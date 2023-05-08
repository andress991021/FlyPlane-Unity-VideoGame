using System.Collections;
using System.Collections.Generic;
using UnityEngine;

//
public class Radar : MonoBehaviour, IEventListener
{
    public RectTransform Coordinate;
    private DynamicsData lastDynamics = null;
    bool isTrigger = false;
    public void notify(DynamicsData dynamics)
    {
        lastDynamics = dynamics;
        isTrigger = true;
    }

    // Start is called before the first frame update
    void Start()
    {
        GlobalStorage.eventManager.suscribe(this);
    }

    // Update is called once per frame
    void Update()
    {
        if (!isTrigger || lastDynamics == null) return;
        Coordinate.anchoredPosition = new Vector2(lastDynamics.px, 1-lastDynamics.py) * 100;
        Debug.Log(Coordinate.anchoredPosition);
    }
}
