from polycircles import polycircles
import simplekml
import interop
from auvsi_suas.client import client

'''
example dictionary
{
    1 : {"lat":123, "lon":123, "radius":1234, "height":1234}
}
'''

def creatKml(obsList):
    kml = simplekml.Kml()
    i=0
    for item in obsDict:
        polycircle = polycircles.Polycircle(latitude=item.latitude,
                                            longitude=item.longitude,
                                            radius=item.cylinder_radius,
                                            number_of_vertices=36)
        pol = kml.newpolygon(name=str(i),outerboundaryis=polycircle.to_kml())
        pol.style.polystyle.color = \
                simplekml.Color.changealphaint(200, simplekml.Color.green)
        i = i + 1
    kml.save("obstackle.kml")
    return 


def main():
    client1 = client.Client(url='http://127.0.0.1:8000', username='testuser',password='testpass')
    mission = client1.get_mission(1)
    print(type(mission))
    #soa.creatKml(stat)

if __name__ == 'main':
    main()
    

