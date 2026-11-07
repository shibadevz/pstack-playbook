<script setup lang="ts">
import { withBase } from 'vitepress'

defineProps<{ type: string; label: string; sits: { title: string; link: string }[] }>()
</script>

<template>
  <div class="meta">
    <span class="chip-type" :data-type="type"><i aria-hidden="true"></i>{{ label }}</span>
    <a v-for="s in sits" :key="s.link" class="chip-sit" :href="withBase(s.link)">{{ s.title }}</a>
  </div>
</template>
