import React,{ useState, useEffect} from 'react';
import { StyleSheet, Text, View,Image,Button,TextInput } from 'react-native';




const register = ({route,navigation}) => {
  const { email1 } = route.params;
  console.log(email1)
  const [email, changeEmail] = React.useState(email1); 
  const [pass, changePass] = React.useState("");
  const [conPass, changeConPass] = React.useState("")
    
    
    async function register(email,password,conPass){
        let reg = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w\w+)+$/
        console.log(email,password,conPass)
        if(password!=null&&email!=null&&reg.test(email)===true){
          
          if(password.length>=6&&password.length<=40){
            if(password==conPass){
              var url='http://192.168.43.120:3000/users/adduser'
            
              await fetch(url, {
                method:"POST",
                headers: {
                  'Accept': 'application/json',
                  'Content-Type':'application/json'
                },
                body: JSON.stringify({
                    email: email,
                    password: password,
                    calories:0
                    })
                }).then(response => response.text())
                .then(json => console.log(json))
                
    
              
              console.log("done")
              navigation.navigate("Home", {
                email: email})
            }else{
              alert("Make sure that Password and Confirm Passwords match")
            }
          }else{
            alert("Make sure that Password is more then 6 characters and less then 40")
          }
        }else{
          alert("Make sure that email is correct ")
        }
  
    }
    return(
      <>
      <View style={styles.fixed}> 
        <Image
        style={styles.logo}
        source={require('./image/bakgroundRegister.jpg')}//logo for bcp beach checker
        />
       </View>
        <View View style={styles.LowerView}>
            <TextInput
          placeholder="Email"
          style={styles.email}
          onChangeText={changeEmail}
          value={email}
          placeholderTextColor="rgba(255,255,255,0.5)" 
            />
        <TextInput
          placeholder="Password"
          style={styles.password}
          onChangeText={changePass}
          value={pass}
          secureTextEntry={true}
          placeholderTextColor="rgba(255,255,255,0.5)" 
        />
        <TextInput
          placeholder="Confirm Password"
          style={styles.conpassword}
          onChangeText={changeConPass}
          secureTextEntry={true}
          value={conPass}
          placeholderTextColor="rgba(255,255,255,0.5)" 
        />
        <View style={styles.notiView}>
            <Button key={1}title="register" onPress={() => register(email,pass,conPass)}color="black" /* skip slider and go to home page*/></Button>
            
          </View>
  
        </View>
        </>
    )



}

export default register;
const styles = StyleSheet.create({
    container: {
      flex: 1,
      marginVertical:35,
      height:500,
    },
    notiView:{
      position:"absolute",
      marginVertical:"100%",
      marginHorizontal: "10%",
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
    LowerView:{
        flex:1,
        flexDirection:"column",
        
        marginHorizontal:"15%",
        marginVertical:"50%",
        
        
        
      },
    
      password:{
        fontWeight:"bold",
        backgroundColor:'rgba(0,0,0,0.6)',
        position:"absolute",
        marginVertical:"20%",
        fontSize:20,
        color:"white",
        width:250,
        height:40
      },
      conpassword:{
        fontWeight:"bold",
        backgroundColor:'rgba(0,0,0,0.6)',
        position:"absolute",
        marginVertical:"40%",
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
      logo:{
        
        width: 1000,
        height: 1000,
        
      
      },
  });
  