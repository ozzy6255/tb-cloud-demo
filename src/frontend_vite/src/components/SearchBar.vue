<script setup>
defineProps(['modelValue'])
defineEmits(['update:modelValue'])
</script>

<template>
  <div class="search-wrapper">
    <input 
      type="text" 
      :value="modelValue"
      @input="$emit('update:modelValue', $event.target.value)"
      placeholder="输入代码或名称搜索..."
      class="glass-input"
    />
    <span class="icon">🔍</span>
  </div>
</template>

<style scoped>
.search-wrapper {
  position: relative;
  width: 100%;
  max-width: 500px;
}

.glass-input {
  width: 100%;
  padding: 15px 20px;
  padding-right: 50px; /* Space for icon */
  font-size: 1.1em;
  border: 1px solid var(--glass-border);
  border-radius: 30px;
  background: rgba(255, 255, 255, 0.5);
  backdrop-filter: blur(4px);
  color: var(--text-main);
  outline: none;
  transition: all 0.3s ease;
  box-shadow: inset 0 2px 4px rgba(0,0,0,0.05);
}

.glass-input:focus {
  background: rgba(255, 255, 255, 0.9);
  box-shadow: 0 4px 15px rgba(74, 144, 226, 0.2);
  border-color: var(--primary-color);
}

.icon {
  position: absolute;
  right: 20px;
  top: 50%;
  transform: translateY(-50%);
  font-size: 1.2em;
  opacity: 0.5;
  pointer-events: none;
}
</style>
