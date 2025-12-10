<script setup>
defineProps({
  record: Object
})
</script>

<template>
  <div class="glass-card logistics-card">
    <div class="card-header">
      <span class="icon">📦</span>
      <h3>物流信息</h3>
    </div>
    
    <div class="info-grid">
      <div class="info-item">
        <label>追溯码</label>
        <div class="value code">{{ record.Code }}</div>
      </div>
      
      <div class="info-item">
        <label>发货时间</label>
        <div class="value">{{ record.OutTime || '未知' }}</div>
      </div>
      
      <div class="info-item">
        <label>经销商</label>
        <div class="value">{{ record.DealerName }}</div>
      </div>
      
      <div class="info-item">
        <label>产品名称</label>
        <div class="value">{{ record.ProductName }}</div>
      </div>
      
      <div class="info-item">
        <label>订单号</label>
        <div class="value">{{ record.OrderNo || '无' }}</div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.logistics-card {
  max-width: 600px;
  margin: 30px auto;
  text-align: left;
}

.card-header {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 20px;
  padding-bottom: 15px;
  border-bottom: 2px solid rgba(74, 144, 226, 0.2);
}

.card-header .icon {
  font-size: 2em;
}

.card-header h3 {
  margin: 0;
  color: var(--primary-color);
}

.info-grid {
  display: grid;
  gap: 15px;
}

.info-item {
  display: flex;
  flex-direction: column;
  gap: 5px;
}

.info-item label {
  font-size: 0.85em;
  color: var(--text-secondary);
  font-weight: 600;
}

.info-item .value {
  font-size: 1.1em;
  color: var(--text-main);
  padding: 8px 12px;
  background: rgba(74, 144, 226, 0.05);
  border-radius: 8px;
}

.info-item .value.code {
  font-family: 'Courier New', monospace;
  font-weight: 700;
  color: var(--primary-color);
}
</style>
