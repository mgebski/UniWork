
import React,{ useState}  from 'react';
import { StyleSheet, Text, View,Button,ScrollView,TextInput } from 'react-native';
import MapView, { PROVIDER_GOOGLE,Marker,Polyline } from 'react-native-maps';
import MapViewDirections from 'react-native-maps-directions';
import haversine from "haversine";

  

const mapView = React.createRef();

class startedRoute extends React.Component {
  constructor(props) {
    
    super(props);
    this.state = {
     latitude: 0,
     longitude:0,
     poliLineCords: [],
     distanceTravelled: 0, 
     prevLatLng: {},
     counter:0,
     error: null
    };
   }
   getMapRegion = () => ({
    latitude: this.state.latitude,
    longitude: this.state.longitude,

   });

  componentDidMount() {
  
  
  navigator.geolocation.watchPosition(
    position => {
      const { latitude, longitude } = position.coords
      const { poliLineCords,distanceTravelled } = this.state
      const newCoordinate = {
        latitude,
        longitude
       };
      this.setState({ 
        latitude,
        longitude,
        poliLineCords: poliLineCords.concat([newCoordinate]),
        distanceTravelled: distanceTravelled + this.calcDistance(newCoordinate),
        prevLatLng: newCoordinate
      })
    }, 
    error => console.log(error),
    { 
      enableHighAccuracy: true,
      timeout: 20000,
      maximumAge: 1000,
      distanceFilter: 10
    }
   );
  }
  endRoute(email,calories){
    
    var dis= this.state.distanceTravelled*1000
    var cal = 0.0625 * dis
    alert("calories burnt during the run: "+cal)
    cal=cal+calories
    
    
    var url='http://192.168.43.120:3000/users/updatecalories'
    
    fetch(url, {
        method:"PUT",
        headers: {
          'Accept': 'application/json',
          'Content-Type':'application/json'
        }, 
        body: JSON.stringify({
            calories: cal,
            email: email,
            })
        })
        this.props.navigation.navigate("Home")
      }
  calcDistance = newLatLng => {
    const { prevLatLng } = this.state
    return haversine(prevLatLng, newLatLng) || 0
  };
  render() {
    
    const coordinate = this.props.route.params.coordinate
    const email =this.props.route.params.email
    const cal =this.props.route.params.cal
    
    
  return (
    // below is the view in which the map is stored and coresponding parameter setting for the map
    <>
      
      <View style={styles.TopView}>
        
      <MapView   /*informed,  ref(https://github.com/react-native-maps/react-native-maps/blob/master/docs/mapview.md,https://github.com/react-native-maps/react-native-maps)*/ 
        provider={PROVIDER_GOOGLE}
        ref={mapView}
        style={styles.map}
        camera={{
        center:{
          latitude: coordinate[0]["latitude"],
          longitude: coordinate[0]["longitude"],
        },
        pitch:1,
        heading:0,
        altitude: 1,
        zoom:13,
        }}
        showsPointsOfInterest={false}
        rotateEnabled={false}
        
          
      >
      <Marker coordinate={this.getMapRegion()} ><View style={styles.m}><Text style={styles.markerText}>You</Text></View></Marker>
      <Polyline coordinates={this.state.poliLineCords} strokeWidth={5} />
      <MapViewDirections
      origin={coordinate[2]}
      destination={coordinate[0]}
      apikey={"AIzaSyB1w34e3tiU7VxbL1iijWLwyhd-K7259XI"}
      strokeWidth={3}
      strokeColor="red"        
      mode={"WALKING"}
      precision={"low"}
      onStart={(params) => {
        console.log(`Started routing between "${params.origin}" and "${params.destination}"`);
      }}
      
      />
      
      <MapViewDirections
      origin={coordinate[1]}
      destination={coordinate[2]}
      apikey={"AIzaSyB1w34e3tiU7VxbL1iijWLwyhd-K7259XI"}
      strokeWidth={3}
      strokeColor="blue"        
      mode={"WALKING"}
      precision={"low"}
      onStart={(params) => {
        console.log(`Started routing between "${params.origin}" and "${params.destination}"`);
      }}
      
      />
      <MapViewDirections
      origin={coordinate[0]}
      destination={coordinate[1]}
      apikey={"AIzaSyB1w34e3tiU7VxbL1iijWLwyhd-K7259XI"}
      strokeWidth={3}
      strokeColor="green"        
      mode={"WALKING"}
      precision={"low"}
      onStart={(params) => {
        console.log(`Started routing between "${params.origin}" and "${params.destination}"`);
      }}
      
      />
    </MapView>
      
          
      </View>
      <View style={styles.marker}>
        
        <Button title="End" onPress={() =>this.endRoute(email,cal) }color="black" /* skip slider and go to home page*/></Button>
        <View style={styles.marker1}>
        <Text style={styles.text}>Distance walked {parseFloat(this.state.distanceTravelled).toFixed(2)} km</Text>
      </View>
      </View>
      <View style={styles.box}>
        <Text style={styles.legend}>Start at green line</Text>
      </View>
      
    </>
  )
  
    }
};




export default startedRoute;

const styles = StyleSheet.create({
    container: {
      ...StyleSheet.absoluteFillObject,
      height: 200,
      width: 200,
      
      alignItems: 'center',
      
    },
   
    TopView:{
      flexDirection:"row",
      width:220,
      height:50,
      marginHorizontal:100,
      alignItems:"center",
      justifyContent: "space-evenly",
      
    },
    
    
    map: {
      ...StyleSheet.absoluteFillObject,
      marginHorizontal:-100,
      marginVertical:80,
      height: 700,
      width: 395,
      
    },
    marker:{
       position:"absolute",
       
       marginHorizontal:150,
       marginVertical:600
       
        
    },
    marker1:{
      position:"absolute",
      backgroundColor: 'rgba(0,0,0,0.6)',
      borderRadius: 4,
      borderWidth: 0.5,
      borderColor: '#000',
      padding: 10,
      margin: 20,
      marginHorizontal: -70,
      marginVertical: 50,
      width:190,
      height:30
     
      
       
   },
   text:{
     position:"absolute",
     fontSize:15,
     color:"white"
   },
   m:{
    paddingVertical: 5,
    paddingHorizontal: 5,
    borderColor: "#eee",
    borderRadius: 5,
    backgroundColor:"rgba(240,248,255,0.95)"
   },
   markerText:{
     fontSize:7
   },
   legend:{
     position:"absolute",
     color:"white"
   },
   box:{
    position:"absolute",
    backgroundColor: 'rgba(0,0,0,0.6)',
    borderRadius: 4,
    borderWidth: 0.5,
    borderColor: '#000',
    padding: 10,
    margin: 20,
    width:140,
    height:0,
    marginVertical:70,
    marginHorizontal:110
   }
  
    
  
    
  });
  