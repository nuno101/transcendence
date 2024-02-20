<!-- <script setup>
import Map from '../components/game/GameMap.vue';
import Paddle from '../components/game/GamePaddle.vue';
import BallandScores from '../components/game/GameBallandScores.vue';
import { ref, reactive } from 'vue';

  const mapWidth = 624;
  const mapHeight = 351;
  let canvas = ref(null);
  let context = ref(null);
const paddle1 = reactive({
  x: 0,
  y: 0,
  width: 0,
  height: 0,
  color: ''
});

const paddle2 = reactive({
  x: 0,
  y: 0,
  width: 0,
  height: 0,
  color: ''
});

  const handleCanvasUpdate = (updateCanvas) => {
    canvas.value = updateCanvas;
    context.value = updateCanvas.getContext('2d');
  };
</script> -->

<template>
  <div class="container d-flex justify-content-center align-items-center">
    <canvas ref="canvas"></canvas>
    <div class="middle-line"></div>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue';
import Vector from '../js/Vector'

const canvas = ref(null)
const keys = new Set()

const getMousePos = (canvas, evt) => {
  var rect = canvas.getBoundingClientRect()
  return new Vector(evt.clientX - rect.left, evt.clientY - rect.top)
}

const handleKeys = (speed) => {
  var direction = new Vector(0.0, 0.0)
  
  if (keys.has('w'))
  direction.y -= speed
if (keys.has('s'))
direction.y += speed
if (keys.has('a'))
direction.x -= speed
if (keys.has('d'))
direction.x += speed

return direction
}

class Scene {
  init(canvas, width, height) {
    this.canvas = canvas
    this.width = width
    this.height = height
    this.canvas.width = width
    this.canvas.height = height
    this.ctx = this.canvas.getContext('2d')
    this.translate = new Vector(this.width / 2, this.height / 2)
  }
  clear() {
    this.ctx.clearRect(0, 0, this.width, this.height)
  }
  transform(v) {
    return new Vector(v.x * this.translate.y + this.translate.x, v.y * this.translate.y + this.translate.y)
  }
  drawLine(a, b, color = 'white', lineWidth = 5) {
    const a1 = this.transform(a)
    const b1 = this.transform(b)

    this.ctx.beginPath()
    this.ctx.moveTo(a1.x, a1.y)
    this.ctx.lineTo(b1.x, b1.y)
    this.ctx.strokeStyle = color
    this.ctx.lineWidth = lineWidth
    this.ctx.stroke()
  }
  drawCircle(position, radius, color = 'white', lineWidth = 5) {
    const position1 = this.transform(position)
    const radius1 = radius * this.translate.y
    this.ctx.beginPath()
    this.ctx.moveTo(position1.x + radius1, position1.y)
    this.ctx.arc(position1.x, position1.y, radius1, 0, Math.PI * 2, true)
    this.ctx.strokeStyle = color
    this.ctx.lineWidth = lineWidth
    this.ctx.stroke()
  }
  normalize(v) {
    v.x -= scene.translate.x
    v.x /= scene.translate.y 
    v.y -= scene.translate.y
    v.y /= scene.translate.y
  }
}

var timeOfLastFrame = 0.0
var mousePos = new Vector(0, 0)
var playerPos = new Vector(0.0, 0.0)
var playerRadius = 0.1
var mouseUp = false
var move = new Vector(0, 0)
var shouldMove = 0.0
var pause = false
var lastKeyPress = 0.0
const scene = new Scene()
const lines = {
  top: [
    // {
    //   a: new Vector(-0.5, 0.5),
    //   b: new Vector(0.5, 0.5)
    // }
  ],
  bottom: [
    {
      a: new Vector(-0.5, -0.5),
      b: new Vector(0.5, -0.5)
    }
  ],
  right: [
    // {
    //   a: new Vector(-0.5, -0.5),
    //   b: new Vector(-0.5, 0.5),
    // },
  ],
  left: [
    {
      a: new Vector(0.5, -0.5),
      b: new Vector(0.5, 0.5),
    },
    {
      a: new Vector(playerRadius, -0.5),
      b: new Vector(playerRadius, 0.5),
    },
  ]
}
const sides = [
  {
    filter: (direction) => {
      return direction.y < 0
    },
    delta: new Vector(0, -playerRadius),
    side: 'bottom'
  },
  {
    filter: (direction) => {
      return direction.y > 0
    },
    delta: new Vector(0, playerRadius),
    side: 'top'
  },
  {
    filter: (direction) => {
      return direction.x < 0
    },
    delta: new Vector(-playerRadius, 0),
    side: 'right'
  },
  {
    filter: (direction) => {
      return direction.x > 0
    },
    delta: new Vector(playerRadius, 0),
    side: 'left'
  }
]

const collidesWithLine = (position, direction, line, horizontalLine) => {
  let factor
  if (horizontalLine)
    factor = Vector.factorToYOf(line.a.y, position, direction)
  else
    factor = Vector.factorToXOf(line.a.x, position, direction)

  if (factor < 0 || factor > 1) return 1
  let intersection = direction.clone()
  intersection.scalarMul(factor)
  intersection.add(position)
  if (horizontalLine) {
    if (intersection.x < Math.min(line.a.x, line.b.x) || intersection.x > Math.max(line.a.x, line.b.x))
      return 1
  } else {
    if (intersection.y < Math.min(line.a.y, line.b.y) || intersection.y > Math.max(line.a.y, line.b.y))
      return 1
  }
  return factor
}

const calcLine = (position, direction) => {
  const sideFiltered = sides.filter((side) => { return side.filter(direction) })

  let lowestFactor = 1
  let sideOfLowestFactor

  sideFiltered.forEach((side) => {

    const deltaPos = position.clone()
    const deltaDir = direction.clone()
    deltaPos.add(side.delta)

    lines[side.side].forEach((line) => {
        let factor = collidesWithLine(deltaPos, deltaDir, line, side.side === 'top' || side.side === 'bottom')
        if (factor < lowestFactor) {
          lowestFactor = factor
          sideOfLowestFactor = side
        }
    })
  })
  
  if (lowestFactor !== 1) {
    const start = position.clone()
    const circle = direction.clone()
    circle.scalarMul(lowestFactor)
    circle.add(position)
    scene.drawCircle(circle, playerRadius, 'green')    
    start.add(sideOfLowestFactor.delta)

    const dirBeforeIntersection = direction.clone()
    dirBeforeIntersection.scalarMul(lowestFactor)
    position.add(dirBeforeIntersection)

    dirBeforeIntersection.add(start)
    scene.drawLine(start, dirBeforeIntersection, 'green')
    
    // after intersection
    direction.scalarMul(1 - lowestFactor)
    if (sideOfLowestFactor.side === 'top' || sideOfLowestFactor.side === 'bottom') {
      direction.y *= -1
    } else {
      direction.x *= -1
    }
    
    calcLine(position, direction)
  } else {
    const end = direction.clone()
    end.add(position)
    scene.drawLine(position, end, 'blue')

    position.add(direction)
    scene.drawCircle(position, playerRadius, 'blue')
  }
}

const calcMove = (position, direction, move) => {
  const sideFiltered = sides.filter((side) => { return side.filter(direction) })

  let lowestFactor = 1
  let sideOfLowestFactor

  sideFiltered.forEach((side) => {

    const deltaPos = position.clone()
    deltaPos.add(side.delta)

    lines[side.side].forEach((line) => {
        let factor = collidesWithLine(deltaPos, direction, line, side.side === 'top' || side.side === 'bottom')
        if (factor < lowestFactor) {
          lowestFactor = factor
          sideOfLowestFactor = side
        }
    })
  })
  
  if (lowestFactor !== 1) {
    const dirBeforeIntersection = direction.clone()
    dirBeforeIntersection.scalarMul(lowestFactor)
    position.add(dirBeforeIntersection)
    
    direction.scalarMul(1 - lowestFactor)
    if (sideOfLowestFactor.side === 'top' || sideOfLowestFactor.side === 'bottom') {
      direction.y *= -1
      move.y *= -1
    } else {
      direction.x *= -1
      move.x *= -1
    }
    
    calcLine(position, direction, move)
  } else {
    position.add(direction)
  }
}

const instantMove = false

const loop = (timeOfCurrentFrame) => {
  const deltaTime = timeOfCurrentFrame - timeOfLastFrame
  timeOfLastFrame = timeOfCurrentFrame

  scene.clear()

  const speed = deltaTime * 0.001
  
  
  const dir = handleKeys(speed)


  const mouseDir = mousePos.clone()
  scene.normalize(mouseDir)
  mouseDir.sub(playerPos)
  calcLine(playerPos.clone(), mouseDir.clone())

  if (mouseUp) {
    shouldMove = mouseDir.length()
    move = mouseDir.clone()
    if (!instantMove) move.normalize()
    mouseUp = false
  }

  const deltaTimeMove = move.clone()
  if (!instantMove) deltaTimeMove.scalarMul(speed)

  if (shouldMove) {
    const shoudlMoveInstead = shouldMove
    shouldMove -= deltaTimeMove.length()
    if (shouldMove < 0) {
      deltaTimeMove.normalize()
      deltaTimeMove.scalarMul(shoudlMoveInstead)
      shouldMove = 0.0
    }
  }

  calcMove(playerPos, deltaTimeMove, move)
  playerPos.add(dir)

  if (!shouldMove) {
    move = new Vector(0, 0)
  }

  scene.drawCircle(playerPos, playerRadius, 'white', 2)
  
  for (let side in lines) {
    lines[side].forEach((line) => {
      scene.drawLine(line.a, line.b)
    })
  }

  if (timeOfLastFrame - lastKeyPress > 10000) pause = true

  if (!pause) {
    requestAnimationFrame(loop)
  } else {
    scene.ctx.beginPath()
    scene.ctx.font = '64px serif'
    scene.ctx.fillStyle = 'white'
    scene.ctx.textAlign = 'center'
    scene.ctx.fillText('Paused', canvas.value.width / 2, canvas.value.height / 2)
  }
}

onMounted(() => {  
  document.onmousemove = (evt) => {
    lastKeyPress = timeOfLastFrame
    mousePos = getMousePos(canvas.value, evt)
    if (pause) {
      pause = false
      requestAnimationFrame(loop)
    }
  }
  document.onkeydown = (evt) => {
    
    keys.add(evt.key.toLowerCase())
    if (evt.key === ' ')
    {
      pause = !pause
      if (!pause) requestAnimationFrame(loop)
    }
  }
  document.onkeyup = (evt) => {
    lastKeyPress = timeOfLastFrame
    keys.delete(evt.key.toLowerCase())
  }
  document.onmouseup = (evt) => {
    lastKeyPress = timeOfLastFrame
    mouseUp = true
  }

  scene.init(canvas.value, 800, 600)
  requestAnimationFrame(loop)
})
</script>

<style scoped>
canvas {
    border: 1px solid black;
    position: absolute;
    top: 20%;
    background: #111111;
    width: 800px;
    height: 600px;
}

.middle-line {
  position: absolute;
  top: 20%;
  left: 50%;
  width: 2px;
  height: 600px;
  background: repeating-linear-gradient(
    to bottom,
    #fff,
    #fff 14px,
    #0000 14px,
    #0000 28px
  );
}
</style>
