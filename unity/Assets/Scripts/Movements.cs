using System.Collections;
using System.Collections.Generic;
using UnityEditor;
using UnityEngine;
using UnityEngine.Timeline;
//using WebSocketSharp;
using WebSocketSharp;

public class Movements : MonoBehaviour
{
  
    public CharacterController controller;
    public float speed = 20f;
    public GameObject emptyObject;

    private WebSocket ws;

    void Start()
    {
        ws = new WebSocket("ws://localhost:8765");
        ws.OnMessage += OnMessage;
        ws.Connect();
    }

    void OnMessage(object sender, MessageEventArgs e)
    {
        Debug.Log("Received time: " + e.Data);
    }

    void OnDestroy()
    {
        ws.Close();
    }


    // Update is called once per frame
    void Update()
    {


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
