using System.Collections;
using System.Collections.Generic;
using UnityEditor;
using UnityEngine;
using UnityEngine.Timeline;

public class Movements : MonoBehaviour
{
  
    public CharacterController controller;
    public float speed = 5f;
    public float xSpeed = 1f;
    public GameObject emptyObject;

    // Update is called once per frame
    void Update()
    {
        //Initial Variable
        float x = Input.GetAxis("Horizontal") ;
        float z = 2f;
        float y = Input.GetAxis("Vertical") ;

        float rotatez = 0f;

        float rotatey = 90f;
        float rotationIncrement = Time.time * 5f;
        rotatey += x * rotationIncrement;



        //Movement
        Vector3 movement = transform.right * x + transform.forward * z + transform.up * y;
        controller.Move(movement *speed* Time.deltaTime);

        //Fixed Rotate  
        emptyObject.transform.eulerAngles = new Vector3(0, rotatey, rotatez);
        transform.eulerAngles = new Vector3(0, rotatey, rotatez);
     
    }
}
