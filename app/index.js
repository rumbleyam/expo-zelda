import React, {useEffect} from 'react';
import { StatusBar } from 'expo-status-bar';
import { StyleSheet } from 'react-native';
import {Typography, Colors, Spacings, View, TextField, Text, Button, Image} from 'react-native-ui-lib';
import { SplashScreen } from 'expo-router';

import { useFonts } from 'expo-font';
import _ from 'lodash';

Colors.loadColors({
    black: '#1D1D1D',
    white: '#EEEEEE',
    gray: '#494B4B',
    darkGreen: '#0E5135',
    green: '#0d9263',
    lightGreen: '#4ABA91',
    gold: '#D4CE46',
    red: '#D71627',
    lightPurple: '#A5AEED',
    tan: '#AB9856'
});
  
Typography.loadTypographies({
    h1: {fontSize: 58},
    h2: {fontSize: 46},
    h3: {fontSize: 34},
    h4: {fontSize: 22},
    h5: {fontSize: 10},
});

Spacings.loadSpacings({
    page: 20
});

const colorOptions = [
    Colors.darkGreen,
    Colors.lightPurple,
    Colors.gold,
    Colors.gray,
    Colors.green,    
    Colors.tan,
    Colors.lightGreen,
];

export default function App() {
    const [isReady, setReady] = React.useState(false);
    const [backgroundColor, setBackgroundColor] = React.useState(Colors.darkGreen);

    const [fontsLoaded] = useFonts({
        'dx': require('../assets/fonts/dx.ttf'),
        'triforce': require('../assets/fonts/triforce.ttf'),
        'wild': require('../assets/fonts/wild.otf'),
    });

    const randomizeBackgroundColor = () => {
        setBackgroundColor(_.sample(colorOptions))
    }

    useEffect(() => {
        randomizeBackgroundColor()
    }, [])
    
    useEffect(() => {
        if(fontsLoaded) {
            setReady(true);
        }
    }, [fontsLoaded]);
    return (
        <>
            {!isReady && <SplashScreen />}
            <View style={{backgroundColor}} flex center>
            <Text h1 red style={styles.triforce}>Ravi!</Text>
            <Button background-gray marginT-20 label='Zelda stuff awaits' labelStyle={styles.dx} onPress={randomizeBackgroundColor} />
            <Text h2 black marginT-20 style={styles.wild}>I don't know what</Text>
            <StatusBar style="auto" />
            <Image tintColor={Colors.white} style={[StyleSheet.absoluteFill, styles.image]} source={require('../assets/triforce_pattern.png')} resizeMode='repeat' />
            </View>
        </>
    );
}
    
const styles = StyleSheet.create({
    triforce: {
        fontFamily: 'triforce'
    },
    dx: {
        fontFamily: 'dx',
    },
    wild: {
        fontFamily: 'wild',
    },
    image: {
        height: '100%',
        width: '100%',
        zIndex: -1,
        opacity: 0.25
    }
});