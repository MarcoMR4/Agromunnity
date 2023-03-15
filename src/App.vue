<script setup>
import { RouterLink, RouterView } from 'vue-router'

</script>

<template>
  <header class="navbar sticky-top flex-md-nowrap p-0 shadow justify-content-center">
    <div class="text-center col-md-2 col-lg-1">
      <img src="@/assets/logo.svg" alt="logo" width="20" />
      <p>Agromunnity</p>
    </div>
    <button class="navbar-toggler position-absolute d-md-none collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#sidebarMenu" aria-controls="sidebarMenu" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
  </header>
  <RouterView />
</template>

<style scoped>

.navbar .navbar-toggler {
  top: .25rem;
  right: 1rem;
}

.navbar {
  background-color: #a5e244;
  padding: .75rem 1rem;
  border-width: 0;
  border-radius: 0;
}
</style>
