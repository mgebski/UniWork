import React,{ useState}  from 'react';
import { StyleSheet, Text, View,Button,ScrollView,TextInput } from 'react-native';
import MapView, { PROVIDER_GOOGLE,Marker } from 'react-native-maps';
import MapViewDirections from 'react-native-maps-directions';



    

  

  


const map = ({route,navigation}) => {


const[loading,upLoading]=useState(0)
const mapView = React.createRef();//create a ref varbiale to mention inside the map 

const { lat,long,dist,email,cal } = route.params;

var firstLineRandomNumber = Math.floor(Math.random() * 8)

var secondLineRandomNumber = Math.floor(Math.random() * 8)
while(firstLineRandomNumber==secondLineRandomNumber){
  var secondLineRandomNumber = Math.floor(Math.random() * 8)
  
}
var bLineCounter = 0
while(bLineCounter==0){
  if (firstLineRandomNumber==0 && secondLineRandomNumber!=0 && secondLineRandomNumber!=1 && secondLineRandomNumber!=7 && secondLineRandomNumber!=5){
    bLineCounter = 1
  
  }else if (firstLineRandomNumber==1 && secondLineRandomNumber!=1 && secondLineRandomNumber!=0 && secondLineRandomNumber!=6 && secondLineRandomNumber!=4){
    bLineCounter = 1
  }
  else if (firstLineRandomNumber==3 && secondLineRandomNumber!=3 && secondLineRandomNumber!=2 && secondLineRandomNumber!=5 && secondLineRandomNumber!=4){
    bLineCounter = 1
  }
  else if (firstLineRandomNumber==2 && secondLineRandomNumber!=2 && secondLineRandomNumber!=3 && secondLineRandomNumber!=6 && secondLineRandomNumber!=7){
    bLineCounter = 1
  }
  else if (firstLineRandomNumber==6 && secondLineRandomNumber!=6 && secondLineRandomNumber!=5 && secondLineRandomNumber!=1 && secondLineRandomNumber!=7 && secondLineRandomNumber!=2 && secondLineRandomNumber!=4){
    bLineCounter = 1
  } 
  else if (firstLineRandomNumber==7 && secondLineRandomNumber!=7 && secondLineRandomNumber!=4 && secondLineRandomNumber!=6 && secondLineRandomNumber!=5 && secondLineRandomNumber!=2 && secondLineRandomNumber!=0){
    bLineCounter = 1
  }
  else if (firstLineRandomNumber==4 && secondLineRandomNumber!=4 && secondLineRandomNumber!=7 && secondLineRandomNumber!=6 && secondLineRandomNumber!=1 && secondLineRandomNumber!=3 && secondLineRandomNumber!=5){
    bLineCounter = 1
  }
  else if (firstLineRandomNumber==5 && secondLineRandomNumber!=5 && secondLineRandomNumber!=6 && secondLineRandomNumber!=3 && secondLineRandomNumber!=7 && secondLineRandomNumber!=4 && secondLineRandomNumber!=0){
    bLineCounter = 1
  }else{
    var secondLineRandomNumber = Math.floor(Math.random() * 8)
  }
}

var distanceOfRoute=0
var duration=0

var r=6378137
var distance=dist
var firstLine = distance/3
var secondLine = firstLine/2

var dLat=firstLine/r
var dLon=firstLine/(r*Math.cos(Math.PI*lat/180))
var dLatDouble=secondLine/r
var dLonDouble=secondLine/(r*Math.cos(Math.PI*lat/180))
var latA= lat
var lonA= long


if(firstLineRandomNumber==0){//down
  dLat=dLat*-1
  latA= lat+dLat*180/Math.PI
  
  
}else if (firstLineRandomNumber==1){//top
  latA= lat+dLat*180/Math.PI
  
}
else if (firstLineRandomNumber==2){//left
  dLon= dLon*-1
  lonA= long+dLon*180/Math.PI
  
}else if(firstLineRandomNumber==3){//right
  lonA= long+dLon*180/Math.PI
}else if (firstLineRandomNumber==4){//top right

  latA= lat+dLatDouble*180/Math.PI
  lonA= long+dLonDouble*180/Math.PI
} 
else if(firstLineRandomNumber==5){//bottom right
  dLatDouble=dLatDouble*-1
  latA= lat+dLatDouble*180/Math.PI
  lonA= long+dLonDouble*180/Math.PI
}
else if(firstLineRandomNumber==6){//top left
  dLonDouble= dLonDouble*-1
  latA= lat+dLatDouble*180/Math.PI
  lonA= long+dLonDouble*180/Math.PI
}
else if(firstLineRandomNumber==7){//bottom left
  dLatDouble=dLatDouble*-1
  dLonDouble= dLonDouble*-1
  latA= lat+dLatDouble*180/Math.PI
  lonA= long+dLonDouble*180/Math.PI
}

var dlatB=firstLine/r
var dlonB=firstLine/(r*Math.cos(Math.PI*latA/180))
var dLatDouble1=secondLine/r
var dLonDouble1=secondLine/(r*Math.cos(Math.PI*latA/180))
var latB= latA
var lonB= lonA
if (secondLineRandomNumber==0){//down
  dlatB=dlatB*-1
  latB= latB+dlatB*180/Math.PI
  
  
}else if (secondLineRandomNumber==1 ){//up
  latB= latB+dlatB*180/Math.PI
 
}
else if (secondLineRandomNumber==2 ){//left
  dlonB = dlonB*-1
  lonB= lonB+dlonB*180/Math.PI
 
}
else if (secondLineRandomNumber==3 ){//right
  lonB= lonB+dlonB*180/Math.PI
  
}
else if (secondLineRandomNumber==4 ){//topright
  latB= latB+dLatDouble1*180/Math.PI
  lonB= lonB+dLonDouble1*180/Math.PI
  
} 
else if (secondLineRandomNumber==5 ){//bottom right
  dLatDouble1=dLatDouble1*-1
  latB= latB+dLatDouble1*180/Math.PI
  lonB= lonB+dLonDouble1*180/Math.PI
  
}
else if (secondLineRandomNumber==6 ){//top left
  dLonDouble1= dLonDouble1*-1
  latB= latB+dLatDouble1*180/Math.PI
  lonB= lonB+dLonDouble1*180/Math.PI
  
}
else if (secondLineRandomNumber==7 ){//bottom left
  dLatDouble1=dLatDouble1*-1
  dLonDouble1= dLonDouble1*-1
  latB= latB+dLatDouble1*180/Math.PI
  lonB= lonB+dLonDouble1*180/Math.PI
  
}

  const coordinate =[
    {
      latitude:lat,
      longitude: long
    },
    {
      latitude: latA, 
      longitude: lonA
    },
    {
      latitude:latB,
      longitude: lonB
    }
    
  ]
 


 
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
            latitude: lat,
            longitude: long,
          },
          pitch:1,
          heading:0,
          altitude: 1,
          zoom:13,
          }}
          showsPointsOfInterest={false}
          rotateEnabled={false}
          
            
        >
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
        onReady={result => {
          distanceOfRoute=distanceOfRoute+result.distance
          duration=duration+result.duration
        }
        }
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
        onReady={result => {
          
          distanceOfRoute=distanceOfRoute+result.distance
          duration=duration+result.duration
        }
        }
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
        onReady={result => {
          distanceOfRoute=distanceOfRoute+result.distance
          duration=duration+result.duration
          console.log(distanceOfRoute,duration)
         
         
        }
        }
        />
      </MapView>
        
            
        </View>
        <View style={styles.marker}>
          <Button title="Change route" onPress={() => upLoading(loading+1)}color="black" /* skip slider and go to home page*/></Button>
          <Button title="Start" onPress={() =>navigation.navigate("startedRoute",{coordinate: coordinate,email:email,cal:cal}) }color="black" /* skip slider and go to home page*/></Button>
        </View>
       
      </>
    )
 
 
};




export default map;

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
       
       marginHorizontal:125,
       marginVertical:600,
       
       
        

    },
    marker1:{
      position:"absolute",
      
      marginHorizontal:70,
      marginVertical:600
      
       
   },
  
    
  
    
  });
  