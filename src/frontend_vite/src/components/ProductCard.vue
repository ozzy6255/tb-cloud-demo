<script setup>
defineProps({
  product: Object
})
</script>

<template>
  <div class="glass-card product-card">
    <div class="card-id">#{{ product.ProductId }}</div>
    <div class="card-body">
      <h3 class="product-name">{{ product.ProductName }}</h3>
    </div>
    <div class="card-footer">
      <button class="action-btn">查看详情</button>
    </div>
  </div>
</template>

<style scoped>
.product-card {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  text-align: left;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  overflow: hidden;
  position: relative;
}

.product-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 12px 40px rgba(31, 38, 135, 0.15);
  background: rgba(255, 255, 255, 0.85); /* Whiter on hover */
}

.card-id {
  font-size: 0.8em;
  color: var(--primary-color);
  font-weight: 700;
  margin-bottom: 10px;
  background: rgba(74, 144, 226, 0.1);
  padding: 4px 8px;
  border-radius: 6px;
}

.product-name {
  font-size: 1.2em;
  margin: 0 0 20px 0;
  line-height: 1.4;
  flex-grow: 1; /* Push footer down */
}

.card-footer {
  width: 100%;
}

.action-btn {
  width: 100%;
  background: transparent;
  color: var(--primary-color);
  border: 1px solid var(--primary-color);
}

.action-btn:hover {
  background: var(--primary-color);
  color: white;
}
</style>
