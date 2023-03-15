
<template>
    <body class="color1">
        <div id="layoutAuthentication">
            <div id="layoutAuthentication_content">
                <main>
                    <div class="container">
                        <div class="row justify-content-center">
                            <div class="col-lg-5">
                                <div class="card shadow-lg border-0 rounded-lg mt-5">
                                    <div class="card-header"><h3 class="text-center font-weight-light my-4">Inicia Sesión</h3></div>
                                    <div class="card-body">
                                        <form @submit.prevent="login">
                                            <div class="form-floating mb-3">
                                                <input v-model="email" class="form-control" id="email" type="email" placeholder="Correo" />
                                                <label for="email">Correo</label>
                                            </div>
                                            <div class="form-floating mb-3">
                                                <input v-model="pwd" class="form-control" id="pwd" type="password" placeholder="Contraseña" />
                                                <label for="pwd">Contraseña</label>
                                            </div>
                                            <div class="d-flex align-items-center justify-content-center mt-4 mb-0">
                                                <input value="ingresar" class="btn btn-success" type="submit">
                                            </div>
                                        </form>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </main>
            </div>
            <div id="layoutAuthentication_footer">
                <footer class="py-4 bg-light mt-auto">
                    <div class="container-fluid px-4">
                        <div class="d-flex align-items-center justify-content-center small">
                            <div class="text-muted">Copyright &copy; Agromunnity 2023</div>
                        </div>
                    </div>
                </footer>
            </div>
        </div>
    </body>
</template>

<script>
    import Swal from 'sweetalert2'
    import { getAuth, signInWithEmailAndPassword } from "firebase/auth";
    import router from '../router';
    export default{
        data(){
            return{
                email:'',
                pwd:''
            }
        },
        methods:{
            login(){
                const auth = getAuth();
                signInWithEmailAndPassword(auth, this.email, this.pwd)
                .then((user) => { this.$router.replace('home'); })
                .catch((error) => {
                    Swal.fire({
                    title: 'Error!',
                    text: 'Usuario y/o contraseña invalidos',
                    icon: 'error',
                    confirmButtonColor: "#a5e244",
                    confirmButtonText: 'Reintentar'
                    })
                });
            }

        }
    }

</script>

<style>
    #layoutAuthentication {
        display: flex;
        flex-direction: column;
        min-height: 100vh;
    }
    #layoutAuthentication #layoutAuthentication_content {
        min-width: 0;
        flex-grow: 1;
    }
    #layoutAuthentication #layoutAuthentication_footer {
        min-width: 0;
    }
</style>