import React,{ useState, useEffect} from 'react';
import { StyleSheet, Text, View,Image,Button,TextInput } from 'react-native';



const login = ({navigation}) => {
    



    const [email, changeEmail] = React.useState(""); 
    const [pass, changePass] = React.useState("");

    async function database(email,password){
      let reg = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w\w+)+$/
      if(reg.test(email)===true){
        var url='http://192.168.43.120:3000/users'
        const repsonse = await fetch(url)
        const result = await repsonse.json()
        
      
        var resultLenght= Object.keys(result["data"]).length
        
        
        var optioncounter = 0
        var counter = 0
        var cal =0
        while(counter!=resultLenght){
          if(result["data"][counter]["email"]==email.toString()&&result["data"][counter]["password"]==password.toString()){
            optioncounter=1
            cal = result["data"][counter]["calories"]
            
            counter=resultLenght
          }else if (result["data"][counter]["email"]==email&&password!=result["data"][counter]["password"]){
            optioncounter=2
            counter=resultLenght
            }
          else{
            counter=counter+1
          }
        }
        if(optioncounter==1){
            
            navigation.navigate("Home",{
              email: email,
              calories1: cal})
          
        }else if (optioncounter==2){
            alert("Email and Password dont match")
        }
        else{
          navigation.navigate("register",{ email1:email})
          
        }
      }else{
        alert("incorrect email format")
      }
        
  }
    return(
      <>
      <View style={styles.fixed}> 
        <Image
            style={styles.logo}
            source={require('./image/background.jpg')}//logo for bcp beach checker
          />
      </View>
      <View style={styles.LowerView}>
        
        

        
        <TextInput
        placeholder="Email               "
        style={styles.email}
        value={email}
        onChangeText={changeEmail}
        placeholderTextColor="rgba(255,255,250,0.5)" 
        
      />
       <TextInput
        placeholder="Password        "
        style={styles.password}
        value={pass}
        onChangeText={changePass}
        secureTextEntry={true}
        placeholderTextColor="rgba(255,255,255,0.5)" 
      />
      
        <View style={styles.notiView}>
          <Button title="Log in" onPress={() => database(email,pass)}color="black" /* skip slider and go to home page*/></Button>
          
        </View>


      </View>
      
        
      </>
    )
  }


export default login;
const styles = StyleSheet.create({
    container: {
      flex: 1,
      marginVertical:35,
      height:500,
    },
    logo:{
      
      width: 1000,
      height: 1000,
      
    
    },
    
    LowerView:{
      flex:1,
      flexDirection:"column",
      marginHorizontal:"17%",
      marginVertical:"60%",

      
    },
  
    notiView:{
      position:"absolute",
      marginVertical:"70%",
      marginHorizontal: "8%",
      justifyContent:"space-evenly",
      height:200,
      width:200
    },
    email:{
      fontWeight:"bold",
      backgroundColor:'rgba(0,0,0,0.6)',
      position:"absolute",
      fontSize:20,
      color:"white",
      width:250,
      height:40
    },
    password:{
      fontWeight:"bold",
      backgroundColor:'rgba(0,0,0,0.6)',
      position:"absolute",
      marginVertical:50,
      fontSize:20,
      color:"white",
      width:250,
      height:40
    },
  
    fixed:{
      position: 'absolute',
      top: 0,
      left: 0,
      right: 0,
      bottom: 0,
    },
    
    
  });
  