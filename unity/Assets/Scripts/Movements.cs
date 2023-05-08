using System.Collections;
using System.Collections.Generic;
using UnityEditor;
using UnityEngine;
using UnityEngine.Timeline;
using System.Globalization;





public class Movements : MonoBehaviour, IEventListener
{
    const float vz = 35f;
    const float vhand = 1.8f;
    float vhandThresold = 0.008f;
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

    void moveWithHand() {
        if (!isTrigger || lastDynamics == null) return;

        float vx = lastDynamics.vx;
        float vy = lastDynamics.vy;
        if (Mathf.Abs(vx) < vhandThresold) vx = 0;
        if (Mathf.Abs(vy) < vhandThresold) vy = 0;
        Debug.Log(vx + "  ,  " + vy);

        Vector3 movement = -transform.forward * vhand * vx - transform.up * vhand * vy + transform.right * vz * Time.deltaTime;
        transform.Translate(movement);
        isTrigger = false;
    }

    void moveWithKeyboard() {
        float x = Input.GetAxis("Horizontal") * vz;
        float z = 8f;
        float y = Input.GetAxis("Vertical") * vz;
        Vector3 movement = transform.right * x + transform.forward * z + transform.up * y;
        transform.Translate(movement * Time.deltaTime);
    }


    void Update()
    {
        moveWithHand();//  
        //moveWithKeyboard() //Uncomment this for move the gameobject using the keyboards
    }
}
