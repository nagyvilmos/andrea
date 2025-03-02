import { defineConfig } from 'vite'
import { svelte } from '@sveltejs/vite-plugin-svelte'

// https://vite.dev/config/
export default defineConfig({
  plugins: [svelte()],
  server: {
    proxy: {
      '/api': {
        target: 'http://127.0.0.1:61975',
        changeOrigin: false,
        //rewrite: (path) => path.replace(/^\/api/, '')
      }
    }
  }})
