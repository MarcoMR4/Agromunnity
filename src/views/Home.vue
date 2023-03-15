<script>
  import { getAuth, signOut } from "firebase/auth";
  export default{
    data(){
        return{

        }
    },
    methods:{
        logout(){
          const auth = getAuth();
          auth.signOut().then(() => this.$router.replace('/login'))
        }
    }
  }
</script>

<template>

  <nav id="sidebarMenu" class="col-md-3 col-lg-2 d-md-block bg-light sidebar collapse ">
    <div class="pt-5 nav flex-column align-items-center">
        <img src="../assets/user-icon.svg" alt="logo" width="85" class="rounded-circle"/> Nombre de usuario
    </div>
    <hr class="hr" />
    <div class="position-sticky pt-4">
    <ul class="nav flex-column">
        <li class="nav-item">
          <a>
            <RouterLink to="/home" class="nav-link text-dark">Inicio</RouterLink>
          </a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="">
            --
          </a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="">
            --
          </a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="">
            --
          </a>
        </li>
        <li class="nav-item">
          <a>
            <router-link to="/user-register" class="nav-link text-dark">
              Registrar usuarios
            </router-link>
          </a>
        </li>
        <li class="nav-item">
          <a href="" @click="logout" class="nav-link text-danger">logout</a>
        </li>
    </ul>
    </div>
  </nav>
  <body>
    <div class="container-fluid">
        <div class="row">
            <main class="col-md-9 ms-sm-auto col-lg-10 p-md-4"> 
                <div class="">
                    Bienvenido
                </div>
            </main>
        </div>
    </div>
  </body>
</template>

<style scoped>

  body {
    font-size: .875rem;
  }

  .feather {
    width: 16px;
    height: 16px;
    vertical-align: text-bottom;
  }
  .sidebar {
    position: fixed;
    top: 0;
    bottom: 0;
    left: 0;
    z-index: 100;
    padding: 48px 0 0;
    box-shadow: inset -1px 0 0 rgba(0, 0, 0, .1);
  }

  @media (max-width: 767.98px) {
    .sidebar {
      top: 5rem;
    }
  }

  .sidebar .nav-link {
    font-weight: 500;
    color: #333;
  }

  .sidebar .nav-link .feather {
    margin-right: 4px;
    color: #727272;
  }

  .sidebar .nav-link.active {
    color:#a5e244;;
  }

  .sidebar .nav-link:hover .feather,
  .sidebar .nav-link.active .feather {
    color: inherit;
  }
  .sidebar-sticky {
    position: relative;
    top: 0;
    height: calc(100vh - 48px);
    padding-top: .5rem;
    overflow-x: hidden;
    overflow-y: auto; /* Scrollable contents if viewport is shorter than content. */
  }
</style>
