import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import '@/assets/bootstrap.bundle.min.js'
import '@/assets/bootstrap.min.css'
import 'sweetalert2'

//Implementacion de firebase
import { initializeApp } from "firebase/app";
import { getAuth, onAuthStateChanged } from "firebase/auth";

const firebaseConfig = {
    apiKey: "AIzaSyCorGC0OiLlKNaT6_62Hwk5Ns3Tdbivc-E",
    authDomain: "agromunnity-63a88.firebaseapp.com",
    projectId: "agromunnity-63a88",
    storageBucket: "agromunnity-63a88.appspot.com",
    messagingSenderId: "755863778427",
    appId: "1:755863778427:web:230e7156a95da36b9c5ede",
    measurementId: "G-B9R8QTS2XF"
};

// Initialize Firebase
const app1 = initializeApp(firebaseConfig);
const auth = getAuth();
auth.onAuthStateChanged(function(user){
    const app = createApp(App)

    app.use(router)

    app.mount('#app')
});
