<script setup>
import { defineProps } from 'vue';
import bootstrap from 'bootstrap/dist/js/bootstrap.bundle';

const props = defineProps({
 podium: {
    default: null
  }
});

</script>

<template>
<div class="podium-container">
	<div class="podium__item">
	  <p class="podium__nickname">
		<router-link class="router-link-exact-active" :to="'/users/' + podium[1].id"> 
				{{ podium[1].nickname }}
			</router-link>
		</p>	  
	  <div class="podium__rank second">
        <i class="bi bi-trophy-fill second-medal"></i>
        <span>2</span>
      </div>

	</div>
	<div class="podium__item">
		<p class="podium__nickname">		  
			<router-link class="router-link-exact-active" :to="'/users/' + podium[0].id"> 
				{{ podium[0].nickname }}
			</router-link>
		</p>
	  <div class="podium__rank first">
		<i class="bi bi-trophy-fill first-medal"></i>
        <span class="first-text">1</span>
	  </div>
  </div>
	<div v-if="podium.length > 2" class="podium__item">
	  <p class="podium__nickname">
		<router-link class="router-link-exact-active" :to="'/users/' + podium[2].id"> 
				{{ podium[2].nickname }}
			</router-link>
		</p>
	  <div class="podium__rank third">
		<i class="bi bi-trophy-fill third-medal"></i>
        <span>3</span>
	  </div>
	</div>
</div>
</template>

<style>

.podium-container {
  display: flex;
  align-items: flex-end;
  justify-content: center;
  padding-bottom: 2em;
}


.podium__item {
  width: 200px;
  text-align: center;
}

.podium__rank {
	position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 35px;
  color: #fff;
}

.podium__nickname {
  text-align: center;
  padding: 0 .5rem;
  font-weight: bold;
}

.first {
  min-height: 300px;
  background: #4d20e9;
}

.first-text {
  font-size: 100px;
  font-weight: bold;
}

.second {
  min-height: 200px;
  background: #6145cc;
}

.third {
  min-height: 100px;
  background: #2518a3;
}

.first-medal {
	color: #FFD700;
}

.second-medal {
	color: #C0C0C0;
}

.third-medal {
	color: #CD7F32;
}

.router-link-exact-active {
    color: black;
  }

</style>