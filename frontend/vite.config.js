import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  server: {
    port: 8000,
    proxy: {
      '/rest': {
        target: 'http://localhost:8000',
        ws: true,
        changeOrigin: true,
        secure: false
      },
      '/api': {
        target: 'http://localhost:8000',
        ws: true,
        changeOrigin: true,
        secure: false
      },
      '/auth': {
        target: 'http://localhost:8000',
        ws: true,
        changeOrigin: true,
        secure: false
      },
      '/login': {
        target: 'http://localhost:8000',
        ws: true,
        changeOrigin: true,
        secure: false
      },
      '/logout': {
        target: 'http://localhost:8000',
        ws: true,
        changeOrigin: true,
        secure: false
      },
    }
  }
})
