using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class EventManager 
{
    private List<IEventListener> listeners = new List<IEventListener> ();
    public void suscribe(IEventListener newListener)
    {
        listeners.Add(newListener);
    }

    public void notify(DynamicsData dynamics)
    {
        /*float px = dynamics.px;
        float py = dynamics.py;
        float vx = dynamics.vx;
        float vy = dynamics.vy;
        Debug.Log("px:" + px + "  py:" + py + "   vx:" + vx + "  vy:" + vy);*/
        Debug.Log(listeners.Count);
        foreach (IEventListener listener in listeners) {
            listener.notify(dynamics);
        }
    }
}
