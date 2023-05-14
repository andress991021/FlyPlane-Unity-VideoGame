using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DañoBola : MonoBehaviour
{
    // Start is called before the first frame update
    public float damage;
    public GameObject Player;

    private void OnTriggerEnter(Collider other)
    {
        Debug.Log("Esto es un mensaje");
        Player.GetComponent<BarraVida>().vidaActual -= damage;
        if (other.tag == "Player")
        {
            Player.GetComponent<BarraVida>().vidaActual -= damage;
        }


        if (other.tag=="Enemigo")
        {
            Debug.Log("Esto es un mensaje enemigo");
        }
    }
     

}
