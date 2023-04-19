using System.Collections;
using System.Collections.Generic;
using UnityEditor;
using UnityEngine;
using UnityEngine.Timeline;

public class Movements : MonoBehaviour
{
  
    public CharacterController controller;
    public float speed = 20f;
    public GameObject emptyObject;

    // Update is called once per frame
    void Update()
    {
        //Initial Variable
        float x = Input.GetAxis("Horizontal")*speed ;
        float z = 8f;
        float y = Input.GetAxis("Vertical")*speed ;

        

        //Movement
        Vector3 movement = transform.right * x + transform.forward * z + transform.up * y;
        controller.Move(movement * Time.deltaTime);

        //Fixed Rotate  
        //emptyObject.transform.eulerAngles = new Vector3(0, rotatey, rotatez);
        //transform.eulerAngles = new Vector3(0, rotatey, rotatez);
     
    }
}
