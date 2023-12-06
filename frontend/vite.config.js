import { fileURLToPath, URL } from 'node:url'
import path from 'node:path'// Import path module

const __filename = fileURLToPath(import.meta.url)
const __dirname = path.dirname(__filename)

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue()
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url)),
      '~bootstrap': path.resolve(__dirname, 'node_modules/bootstrap')
    }
  },
  server: {
    proxy: {
      '/api': {
        target: 'http://localhost:8000', // Your Django backend URL
        changeOrigin: true,
        rewrite: path => path.replace(/^\/api/, '') // Remove the '/api' prefix when forwarding the request
      }
    }
  }
})
