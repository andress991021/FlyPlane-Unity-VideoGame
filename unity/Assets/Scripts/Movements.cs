using System.Collections;
using System.Collections.Generic;
using UnityEditor;
using UnityEngine;
using UnityEngine.Timeline;
//using WebSocketSharp;
using WebSocketSharp;
using WebSocketSharp.Server;
using System.Threading;
using System.Globalization;

public class Globals {
    public static string message = "";
    public static bool newDataReceived = false;
}

public class TimeService : WebSocketBehavior
{
    public ManualResetEvent ClientConnectedEvent { get; set; }
    public bool isConnection { get; set; } = false;
    public int times = 0;
   
    protected override void OnOpen()
    {
        ClientConnectedEvent.Set();
    }

    protected override void OnMessage(MessageEventArgs e)
    {
        ClientConnectedEvent.WaitOne(); // Wait for client to connect
        Globals.message = e.Data;
        Globals.newDataReceived = true;
        //Debug.Log(Globals.message + ":"+ times);
        times++;
    }
}


public class Movements : MonoBehaviour
{
  
    public CharacterController controller;
    public float speed = 20f;
    public GameObject emptyObject;

    private WebSocketServer wssv;
    private ManualResetEvent clientConnectedEvent = new ManualResetEvent(false);


    void Start()
    {
        wssv = new WebSocketServer("ws://localhost:8765");
        wssv.AddWebSocketService<TimeService>("/time", () =>
        {
            var service = new TimeService();
            service.ClientConnectedEvent = clientConnectedEvent;
            return service;
        });
        wssv.Start();
    }


    void OnDestroy()
    {
        wssv.Stop();
    }


    // Update is called once per frame
    void Update()
    {

        float x = 0.0f;
        float z = 3f;
        float y = 0.0f;
        float speedHand = 1.3f;
        float thresold = 0.01f;
        if (Globals.newDataReceived)
        {
            string message = Globals.message;
            string[] substrings = message.Split(',');
            x = float.Parse(substrings[0], CultureInfo.InvariantCulture);
            y = float.Parse(substrings[1], CultureInfo.InvariantCulture);
            if (Mathf.Abs(x) < thresold) x = 0;
            if (Mathf.Abs(y) < thresold) y = 0;

            Globals.newDataReceived = false;
        }
        Vector3 movement = transform.right* speedHand * x - transform.up* speedHand * y + transform.forward * z * Time.deltaTime;
        controller.Move(movement);


        //Initial Variable

        //WebSocket


        //Movement
        //Vector3 movement = transform.right * x + transform.forward * z + transform.up * y;
        //controller.Move(movement * Time.deltaTime);

        //Fixed Rotate  
        //emptyObject.transform.eulerAngles = new Vector3(0, rotatey, rotatez);
        //transform.eulerAngles = new Vector3(0, rotatey, rotatez);

    }
}
