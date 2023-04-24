using System.Collections;
using System.Collections.Generic;
using UnityEditor;
using UnityEngine;
using UnityEngine.Timeline;
//using WebSocketSharp;
using WebSocketSharp;
using WebSocketSharp.Server;
using System.Threading;
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
        isConnection = true;       
        Debug.Log(e.Data+":"+ times);
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
        Debug.Log(wssv.WebSocketServices);


        //Initial Variable
        float x = Input.GetAxis("Horizontal")*speed ;
        float z = 4f;
        float y = Input.GetAxis("Vertical")*speed ;
        //WebSocket
        

        //Movement
        Vector3 movement = transform.right * x + transform.forward * z + transform.up * y;
        controller.Move(movement * Time.deltaTime);

        //Fixed Rotate  
        //emptyObject.transform.eulerAngles = new Vector3(0, rotatey, rotatez);
        //transform.eulerAngles = new Vector3(0, rotatey, rotatez);
     
    }
}
