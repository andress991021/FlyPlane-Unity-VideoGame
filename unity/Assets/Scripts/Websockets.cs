using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using WebSocketSharp;
using WebSocketSharp.Server;
using System.Threading;
using System.Globalization;

public class TimeService : WebSocketBehavior
{
    public ManualResetEvent ClientConnectedEvent { get; set; }

    protected override void OnOpen()
    {
        ClientConnectedEvent.Set();
    }

    protected override void OnMessage(MessageEventArgs e)
    {
        ClientConnectedEvent.WaitOne(); // Wait for client to connect
        DynamicsData data = JsonUtility.FromJson<DynamicsData>(e.Data);
        GlobalStorage.eventManager.notify(data);
        
    }
}


public class Websockets : MonoBehaviour
{

    private WebSocketServer wssv;
    private ManualResetEvent clientConnectedEvent = new ManualResetEvent(false);

    void Awake()
    {
        Debug.Log("Open websocket");
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
}
