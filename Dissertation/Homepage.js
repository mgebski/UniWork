import React,{ useState, useEffect} from 'react';
import { StyleSheet, Text, View,Image,Button,TextInput } from 'react-native';
import * as Location from 'expo-location';
import * as Permissions from 'expo-permissions';



const HomePage = ({route,navigation}) => {
  
  const [dist, changeDist] = React.useState("");
  const [cal, upCalories] = React.useState(); 
  const { email,calories1} = route.params;
  
  async function locationPermission(){
     if(dist>=1000){
      let { status } = await Permissions.askAsync(Permissions.LOCATION);//ask user permission for using their curent location
      if (status !== 'granted') {//make sure that if the user didnt give permission the application wouldn't continue
          this.setState({
          errorMessage: 'Permission to access location was denied',
          });
          } 
      else{
        let location = await Location.getCurrentPositionAsync({accuracy:Location.Accuracy.Highest})//get users current location
        const { latitude , longitude } = location.coords
        
        navigation.navigate("map",{ lat:latitude,long:longitude,dist:dist,email:email,cal:calories1})
      }
     }else{
       alert("enter distance bigger or more then 1000m")
     }
   
        
    }
  
  var url='http://192.168.43.120:3000/users/getCalories'
  const calories=()=> fetch(url, {
      method:"POST",
      headers: {
        'Accept': 'application/json',
        'Content-Type':'application/json'
      }, 
      body: JSON.stringify({
          email: email,
          })
      }).then(response => {return response.json()})
      
      
      
  
    

    async function k (){
      let r= await calories()
      upCalories(JSON.stringify(r.data))
    }
    k()
    
    return (
      <>
      <View style={styles.fixed}> 
      <Image
          style={styles.logo}
          source={require('./image/backgroundHomepage.jpg')}//logo for bcp beach checker
        />
    </View>
        <View style={styles.boxSimple}/*box which displays behind the main elements to highlight them*/ >

        </View>
        <View style={styles.LowerView}>
            <Text style={styles.textMain}>Welcome to fitness application</Text>
            <Text style={styles.Notice}>Burned Calories {cal}</Text>
            <TextInput
            placeholder="Enter Distance "
            style={styles.dist}
            value={dist}
            keyboardType='numeric'
            onChangeText={changeDist}
            placeholderTextColor="rgba(255,255,250,0.5)" 
          />
        <View style={styles.refreshButton}>
            <Button title="Refresh" onPress={() => k()}color="black" /* skip slider and go to home page*/></Button>
          </View>   
                
      
            
        </View>
        <View style={styles.ButtonView}>
          <View style={styles.ViewButton}>
          <Button title="Generate Route"color="black"onPress={() =>locationPermission()}/* button to navigate to the map*//>
          <View style={styles.loutoutButton}>
            <Button title="Log out" onPress={() => navigation.navigate("login")}color="black" /* skip slider and go to home page*/></Button>
          </View>
          </View>  
        </View>
      </>
    );
  }

  
export default HomePage;
const styles = StyleSheet.create({
    container: {
      flex: 1,
      marginVertical:35,
      height:500,
    },

    
    LowerView:{
      flex:1,
      flexDirection:"column",
      
      marginHorizontal:60,
      marginVertical:150,
      
      
      
    },
    Notice:{
      fontSize:18,
      color:"white",
      marginHorizontal:"-5%",
      marginVertical:"60%"
    },
   
    
    ButtonView:{
      flex:1,
      flexDirection:'column',
      marginVertical:"-10%",
      marginHorizontal:"6%",
      height:500
      
      
    },
   
    
    ViewButton:{
      width:310,
      height:150,
      
      
      
    },
   
    boxSimple:{
      position:"absolute",
      backgroundColor: 'rgba(0,0,0,0.4)',
      borderRadius: 4,
      borderWidth: 0.5,
      borderColor: '#000',
      padding: 10,
      margin: 20,
      marginVertical:"20%",
      marginHorizontal:"1%",
      width:350,
      height:500
    },
   

    dist:{
      fontSize:20,
      backgroundColor:'rgba(0,0,0,0.6)',
      position:"absolute",
      marginVertical:"100%",
      marginHorizontal:"0%",
      width:250,
      height:50,
      color:"white",
    
    },
    loutoutButton:{
      marginVertical:50
    },
    textMain:{
      position:"absolute",
      marginVertical:"10%",
      color:"white",
      fontSize:20
    },
    fixed:{
      position: 'absolute',
      top: 0,
      left: 0,
      right: 0,
      bottom: 0,
    },
    logo:{
      
      width: 1000,
      height: 1000,
      
    
    },
    refreshButton:{
      position:"absolute",
      marginVertical:"80%",
      marginHorizontal:"30%"
    }
  });
  