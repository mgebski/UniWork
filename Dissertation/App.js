// studentid: S5111611 ubicomp2020 by Maciej Gebski
// This is a redesign from sratch from a application called BCP Beach Check made in react native and expo
import React from 'react';
import { StyleSheet} from 'react-native';
import HomePage from "./Homepage";
import map from "./map";
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import register from "./register";
import login from './login';
import startedRoute from './startedRoute';


const Stack = createStackNavigator();//create a navigation state

export default function App(){
    
  
    return (
    
      <NavigationContainer >
        <Stack.Navigator>
         <Stack.Screen  
            name="login"
            component={login}
            options={{headerStyle: {backgroundColor: 'rgba(0,0,0,0.9)',},headerTintColor: '#fff',headerTitleAlign:"center",headerStatusBarHeight:30, headerLeft: ()=> null}}
          />
          <Stack.Screen
            name="Home"
            component={HomePage}
            options={{headerStyle:{backgroundColor: 'rgba(0,0,0,0.9)',},headerTintColor: '#fff',headerTitleAlign:"center",headerStatusBarHeight:30, headerLeft: ()=> null}}
          />
          <Stack.Screen  
            name="map"
            component={map}
            options={{headerTransparent:true,headerTitleAlign:"center",headerStatusBarHeight:30}}
          />
           <Stack.Screen  
            name="register"
            component={register}
            options={{headerStyle:{backgroundColor: 'rgba(0,0,0,0.9)',},headerTintColor: '#fff',headerTitleAlign:"center",headerStatusBarHeight:30}}
          />
          <Stack.Screen  
            name="startedRoute"
            component={startedRoute}
            options={{headerTransparent:true,headerTitleAlign:"center",headerStatusBarHeight:30}}
          />
          
          
        </Stack.Navigator>
      </NavigationContainer>
    );
  };
  




const styles = StyleSheet.create({
  container: {
    flex: 1,
    marginVertical:35,
    height:500,
    flexDirection:'column',
    backgroundColor: '#fff',
    justifyContent:"center"
    
  }
  
  
  
});
