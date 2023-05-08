using System.Collections;
using System.Collections.Generic;
using UnityEditor;
using UnityEngine;
using UnityEngine.Timeline;
using System.Globalization;





public class Movements : MonoBehaviour, IEventListener
{
    const float vz = 15f;
    const float vhand = 1.8f;
    float vhandThresold = 0.01f;
    private DynamicsData lastDynamics = null;
    bool isTrigger = false;

    public void notify(DynamicsData dynamics)
    {
        lastDynamics = dynamics;
        isTrigger = true;
    }

    void Start()
    {
        GlobalStorage.eventManager.suscribe(this);
    }


    void Update()
    {
        if (!isTrigger || lastDynamics==null) return;

        float px = lastDynamics.px;
        float py = lastDynamics.py;
        float vx = lastDynamics.vx;
        float vy = lastDynamics.vy;

        Vector3 movement = -transform.forward  * vhand * vx - transform.up * vhand * vy + transform.right * vz * Time.deltaTime;
        transform.Translate(movement);
        isTrigger = false;
    }
}
