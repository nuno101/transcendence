<script setup>
import { onMounted, ref, computed, defineProps } from 'vue';
import bootstrap from 'bootstrap/dist/js/bootstrap.bundle';
import router from '../../router';
import Backend from '../../js/Backend';
import PlayerGameAuth from '../auth/PlayerGameAuth.vue';

const currentUser = ref(false);
const isClicked = ref(false);
const games = ref(null);
const gamesInfo = ref(null);
const completedGames = ref(false);
const auth = ref(null);

const props = defineProps({
  title: {
    default: null
  },
  is_Creator: {
    default: null
  },
  tournament_Id: {
    default: null
  }
});

const fetchData = async () => {
	currentUser.value = await Backend.get('/api/users/me');
	games.value = await Backend.get(`/api/tournaments/${props.tournament_Id}/games`);
	console.log("games.value : ", games.value );	
	if (props.title == "Select a game") { // use an integer 
		gamesInfo.value = games.value.filter(game => game.status !== 'done' && game.status !== 'cancel');
	}
	else if (props.title == "Finished games") {
		gamesInfo.value = games.value.filter(game => game.status === 'done' || game.status === 'cancel');
	}

};

const handleGameClick = (index) => {
    isClicked.value = index;
};

document.body.addEventListener('click', (event) => {
    if (!event.target.closest('.tournament-bracket__match')) {
        isClicked.value = 0;
    }
});

const cancelGame = async () => {
  try {
    // Cancel a game
  } catch (err) {
    console.error(err.message);
  }
};

onMounted(() => {
	fetchData();
})

</script>

<template>
	<h3 class="tournament-bracket__round-title">{{ title }}</h3> <!-- NOT IF ALL GAMES ARE DONE -->
	<ul v-if="gamesInfo" class="tournament-bracket__list">
		<li v-for="(game, index) in gamesInfo" :key="index" class="tournament-bracket__item">
			<div class="tournament-bracket__match" :class="{ 'user-not-player': (currentUser.nickname !== game.player1.nickname && currentUser.nickname !== game.player2.nickname) || (title === 'Finished games' ) }" tabindex="0" @click="handleGameClick(index + 1)">						
				<table class="tournament-bracket__table">
					<tbody class="tournament-bracket__content">
						<tr class="tournament-bracket__team" :class="{ 'tournament-bracket__team--winner': game.player1_score > game.player2_score }">
							<td class="tournament-bracket__country">
								<abbr class="tournament-bracket__code">{{ game.player1.nickname }}</abbr>
							</td>
							<td class="tournament-bracket__score">
								<span class="tournament-bracket__number">{{ game.status === 'done' ? game.player1_score : '_' }}</span>
							</td>
						</tr>
						<tr class="tournament-bracket__team" :class="{ 'tournament-bracket__team--winner': game.player2_score > game.player1_score }">
							<td class="tournament-bracket__country">
								<abbr class="tournament-bracket__code">{{ game.player2.nickname }}</abbr>
							</td>
							<td class="tournament-bracket__score">
								<span class="tournament-bracket__number">{{ game.status === 'done' ? game.player2_score : '_' }}</span>
							</td>
						</tr>
					</tbody>
					<div style="margin-top: 10px;"></div>
					<h3 class="tournament-bracket__round-title">{{ game.status }}</h3>
				</table>
			</div>
												
			<div v-if="isClicked === (index + 1)">
				<button v-if="is_Creator" class="btn btn-danger" @click="cancelGame(isClicked)">Cancel Game</button>
				<button class="btn btn-success" @click="auth.openModal()">Start Game</button>
				<SecondPlayerAuth
					ref="auth"
					:game_id="<insert gameid>"
					/>
			</div>
		</li>	
	</ul>
	<p v-else>No games information available.</p>
</template>

<style>
/*!
 * Responsive Tournament Bracket
 * Copyright 2016 Jakub Hájek
 * Licensed under MIT (https://opensource.org/licenses/MIT)
 */

.tournament-bracket__round {
  display: block;
  margin-left: -3px;
  flex: 1;
}

.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0,0,0,0);
  border: 0;
}

.tournament-bracket {
  display: flex;
  flex-direction: row;
  
  @media (min-width: @breakpoint-sm) {
    flex-direction: row;
  }
}

.tournament-bracket__round-title {
  color: #9e9e9e;
  font-size: 0.95rem;
  font-weight: 400;
  text-align: center;
  font-style: italic;
}

.tournament-bracket__list {
  flex-direction: column;
  flex-flow: column wrap;
  justify-content: center;
  height: 60%;
  min-height: 60%;
  border-bottom: 1px dashed #e5e5e5;
  transition: padding 0.2s ease-in-out, margin 0.2s ease-in-out;
  
  @media (max-width: @breakpoint-xs) {
    padding-bottom: 1em;
    margin-bottom: 1em;
  }
  
  @media (min-width: @breakpoint-sm) {
    margin-bottom: 0;
    padding-bottom: 0;
    border-right: 1px dashed #e5e5e5;
    border-bottom: 0;
  }
  
  .tournament-bracket__round:last-child & {
    border: 0;
  }
}

.tournament-bracket__item {
  display: flex;
  flex: 0 1 auto;
  justify-content: center;
  flex-direction: column;
  align-items: flex-start;
  position: relative;
  padding: 2% 0;
  width: 48%;
  transition: padding 0.2s linear;
  
  &:nth-child(odd) {
    margin-right: 2%;
  }
  
  &:nth-child(even) {
    margin-left: 2%;
  }
  
  &::after {
    transition: width 0.2s linear;
  }
  
  @media (max-width: @breakpoint-xs) {
    width: 100%;
    
    &:nth-child(odd),
    &:nth-child(even) {
      margin-left: 0;
      margin-right: 0;
    }
  }
  
  @media (min-width: @breakpoint-sm) {
    padding: 0.5em 1em;
    width: 100%;
    
    &:nth-child(odd),
    &:nth-child(even) {
      margin: 0;
    }
    
    &::after {
      position: absolute;
      right: 0;
      content: '';
      display: block;
      width: 1em;
      height: 45%;
      border-right: 2px solid #9e9e9e;
    }

    &:nth-child(odd)::after {
      top: 50%;
      border-top: 2px solid #9e9e9e;
      transform: translateY(-1px);
      
      .tournament-bracket--rounded & {
        border-top-right-radius: 0.6em;
      }
    }
    
    &:nth-child(even)::after {
      bottom: 50%;
      border-bottom: 2px solid #9e9e9e;
      transform: translateY(1px);
      
      .tournament-bracket--rounded & {
        border-bottom-right-radius: 0.6em;
      }
    }
    .tournament-bracket__round:first-child & {
       padding-left: 0;
    }
    .tournament-bracket__round:last-child & {
       padding-right: 0;

       &::after {
         display: none;
       }
    }

    .tournament-bracket__round:nth-last-child(2) & {
      &::after {
        border-radius: 0;
        border-right: 0;
      }
    }  
  }
  
  @media (min-width: @breakpoint-lg) {
    padding: 0.5em 1.5em;
    
    &::after {
      width: 1.5em;
    }
  }
}


.tournament-bracket__match {
  display: flex;
  width: 200%;
  background-color: #ffffff;
  padding: 1.5em;
  padding-bottom: 0.5em;
  border: 1px solid transparent;
  border-radius: 0.2em;
  box-shadow: 0 2px 0 0 #e5e5e5;
  outline: none; 
  cursor: pointer;
  transition: padding 0.2s ease-in-out, border 0.2s linear, background-color 0.2s ease-in-out;

  &:focus {
	background-color: #2196F3;
    border-color: #2196F3;
  }
  
  &::before,
  &::after {
    transition: all 0.2s linear;
  }
  
  @media (max-width: @breakpoint-xs) {
    padding: 0.75em 0.5em;
  }
  
  @media (min-width: @breakpoint-sm) {
    &::before,
    &::after {
      position: absolute;
      left: 0;
      z-index: 1;
      content: '';
      display: block;
      width: 1em;
      height: 10%;
      border-left: 2px solid #9e9e9e;
    }

    &::before  {
      bottom: 50%;
      border-bottom: 2px solid #9e9e9e;
      transform: translate(0, 1px);
      
      .tournament-bracket--rounded & {
        border-bottom-left-radius: 0.6em;
      }
    }

    &::after  {
      top: 50%;
      border-top: 2px solid #9e9e9e;
      transform: translate(0, -1px);
      
      .tournament-bracket--rounded & {
        border-top-left-radius: 0.6em;
      }
    }
  }
  
  @media (min-width: @breakpoint-lg) {
    &::before,
    &::after {
      width: 1.5em;
    }
    
    &::before {
      transform: translate(0, 1px);
    }
    
    &::after {
      transform: translate(0, -1px);
    }
  }
}

.user-not-player {
  background-color: #00000009;;
  cursor: not-allowed;
  pointer-events: none;
}


.done {
  background-color: #00000009;;
  cursor: not-allowed;
  pointer-events: none;
}

.tournament-bracket__round:last-child .tournament-bracket__match {
  &::before,
  &::after {
    border-left: 0;
  }
  
  &::before  {
    border-bottom-left-radius: 0;
  }
  
  &::after  {
    display: none;
  }
}

.tournament-bracket__round:first-child .tournament-bracket__match {
  &::before,
  &::after {
    display: none;
  }
}

.tournament-bracket__content {
  display: flex;
  
  &::after {
    content: ':';
    width: 1em;
    text-align: center;
    padding: 0.2em 0.1em;
    
    @media (min-width: @breakpoint-sm) {
       order: 1;
    }
  }
  
  & .tournament-bracket__team:first-child {
    width: 50%;
    order: 0;
    text-align: right;
    
    @media (min-width: @breakpoint-sm) and (max-width: @breakpoint-md) {
      align-items: flex-end;
    }
    
    & .tournament-bracket__country {
      order: 2;
      justify-content: flex-end;
      
      @media (min-width: @breakpoint-xs) {
        order: 0;
      } 
      
      @media (min-width: @breakpoint-sm) and (max-width: @breakpoint-md) {
        flex-direction: column-reverse;
        align-items: flex-end;
      }
    }
    
    & .tournament-bracket__score {
      order: 0;
      
      @media (min-width: @breakpoint-xs) {
         order: 2;
      }
    }
  }
  
  & .tournament-bracket__team:last-child {
    width: 50%;
    order: 2;
    text-align: left;
    
    @media (min-width: @breakpoint-sm) and (max-width: @breakpoint-md) {
      align-items: flex-start;
    }
    
    & .tournament-bracket__country {
      @media (min-width: @breakpoint-sm) {
        justify-content: flex-start;
      }
      
      @media (min-width: @breakpoint-sm) and (max-width: @breakpoint-md) {
        align-items: flex-start;
      }
    }
    
    .tournament-bracket__code {
      order: 1;
    }
  }
}


.tournament-bracket__table {
  width: 100%;
}

.tournament-bracket__caption {
  font-size: 0.8rem;
  color: #BDBDBD;
  font-weight: 300;
  padding-bottom: 0.75em;
}

.tournament-bracket__team {
  display: flex;
  flex-direction: row-reverse;
  justify-content: space-between;
  
  @media (min-width: @breakpoint-xs) {
    flex-direction: column-reverse;
  }
  
  @media (min-width: @breakpoint-sm) {
    flex-direction: column-reverse;
  }
}

.tournament-bracket__country {
  font-size: 0.95rem;
  display: flex;
  margin-top: 0.5em;
  align-items: center;
  
  @media (max-width: @breakpoint-xs) {
    margin-top: 0;
  }
  
  @media (min-width: @breakpoint-sm) and (max-width: @breakpoint-md) {
    display: flex;
    flex-direction: column;
    
    .tournament-bracket__code {
      margin-top: 0.2em;
    }
  }
}

.tournament-bracket__code {
  padding: 0 0.5em;
  color: #212121;
  font-weight: 600;
  text-transform: uppercase;
  border: 0;
  text-decoration: none;
  transition: padding 0.2s ease-in-out;
  
  @media (max-width: @breakpoint-xs) {
    padding: 0 0.25em;
  }
  
  @media (min-width: @breakpoint-sm) and (max-width: @breakpoint-md) {
    padding: 0;
  }
}

.tournament-bracket__score {
  display: flex;
  align-items: center;
  
  .tournament-bracket__team:first-child & {
    flex-direction: row-reverse;
    padding-left: 0.75em;
  }
  
  .tournament-bracket__team:last-child & {
    padding-right: 0.75em;
  }
}

.tournament-bracket__number {
  display: inline-block;
  padding: 0.2em 0.4em 0.2em;
  border-bottom: 0.075em solid transparent;
  font-size: 0.95rem;
  background-color: #00000021;
  border-color: spin(shade(#00000021, 10%), -10);
  
  .tournament-bracket__team--winner & {
    background-color: #ffee58;
    border-color: spin(shade(#ffee58, 2%), -10);
  }
}

</style>