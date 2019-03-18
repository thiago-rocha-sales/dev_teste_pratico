<template>
  <div id="app">
    
    <nav class="navbar is-info" role="navigation" aria-label="main navigation">
      <div class="navbar-brand">
        <a class="navbar-item" href="https://bulma.io">
          <img src="https://bulma.io/images/bulma-logo.png" width="112" height="28">
        </a>

        <a role="button" class="navbar-burger burger" aria-label="menu" aria-expanded="false" data-target="navbarBasicExample">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div id="navbarBasicExample" class="navbar-menu">
        <div class="navbar-start">
          <a class="navbar-item">
            Home
          </a>

          <!-- <a class="navbar-item"> -->
            <!-- Documentation -->
          <router-link class="navbar-item" to="/plataformas">Plataformas</router-link>
          <!-- </a> -->

          <!-- <div class="navbar-item"> -->
          <router-link class="navbar-item" to="/jogos">Jogos</router-link>
          <!-- </div> -->
        </div>

        <div class="navbar-end">
          <div class="navbar-item">
            <div class="buttons">
              <a class="button is-primary">
                <strong>Sign up</strong>
              </a>
              <a class="button is-light">
                Log in
              </a>
            </div>
          </div>
        </div>
      </div>
    </nav> <!-- navbar -->

    <section class="content">
      <div class="container">
        <router-view></router-view>
      </div> <!-- container -->

    </section> <!-- section -->
    

  </div>
</template>

<script>
// export default {
//   name: 'app',
//   data () {
//     return {
//       msg: 'Welcome to Your Vue.js App'
//     }
//   }
// }
</script>