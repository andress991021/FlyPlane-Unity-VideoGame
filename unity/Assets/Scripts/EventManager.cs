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
        
        foreach (IEventListener listener in listeners) {
            listener.notify(dynamics);
        }
    }
}
