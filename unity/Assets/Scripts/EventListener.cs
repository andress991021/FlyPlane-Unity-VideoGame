using System.Collections;
using System.Collections.Generic;
using UnityEngine;



public interface IEventListener 
{
   /* public void notify(DynamicsData dynamics)
    {
        throw new System.Exception("You must implement this method");
    }*/

    void notify(DynamicsData dynamics);

}
