<script setup>
import { ref, onMounted, computed } from 'vue'
import SearchBar from './components/SearchBar.vue'
import ProductCard from './components/ProductCard.vue'
import LogisticsCard from './components/LogisticsCard.vue'

const products = ref([])
const loading = ref(true)
const searchQuery = ref('')
const error = ref(null)
const logisticsRecord = ref(null)
const searchMode = ref('product') // 'product' or 'logistics'

// API Configuration - use /api prefix for production
const API_URL = import.meta.env.VITE_API_URL || '/api'

const fetchProducts = async () => {
  try {
    loading.value = true
    const response = await fetch(`${API_URL}/products?limit=100`)
    if (!response.ok) throw new Error('API Error')
    products.value = await response.json()
  } catch (err) {
    error.value = "无法连接服务，请确保后端运行中 (Port 8002)"
    console.error(err)
  } finally {
    loading.value = false
  }
}

// Search Logic
const filteredProducts = computed(() => {
  if (!searchQuery.value) return products.value
  const lowerQuery = searchQuery.value.toLowerCase()
  return products.value.filter(p => 
    String(p.ProductId).toLowerCase().includes(lowerQuery) || 
    p.ProductName.toLowerCase().includes(lowerQuery)
  )
})

const searchLogistics = async () => {
  if (!searchQuery.value || searchQuery.value.length < 10) {
    error.value = "请输入完整的追溯码 (至少10位)"
    return
  }
  
  try {
    loading.value = true
    error.value = null
    logisticsRecord.value = null
    
    const response = await fetch(`${API_URL}/logistics?code=${searchQuery.value}`)
    if (!response.ok) {
      if (response.status === 404) {
        error.value = "未找到该追溯码的物流信息"
      } else {
        throw new Error('API Error')
      }
      return
    }
    
    logisticsRecord.value = await response.json()
    searchMode.value = 'logistics'
  } catch (err) {
    error.value = "查询失败,请检查网络连接"
    console.error(err)
  } finally {
    loading.value = false
  }
}

const resetToProducts = () => {
  searchMode.value = 'product'
  logisticsRecord.value = null
  searchQuery.value = ''
  error.value = null
}

onMounted(fetchProducts)
</script>

<template>
  <div class="container">
    <header class="glass-card header">
      <h1>TB 物流查询系统</h1>
      <p class="subtitle">产品查询 & 追溯码物流跟踪</p>
      
      <div class="mode-toggle">
        <button 
          :class="{ active: searchMode === 'product' }" 
          @click="resetToProducts"
        >
          产品查询
        </button>
        <button 
          :class="{ active: searchMode === 'logistics' }" 
          @click="searchMode = 'logistics'; logisticsRecord = null"
        >
          物流追溯
        </button>
      </div>
      
      <SearchBar v-model="searchQuery" />
      
      <button 
        v-if="searchMode === 'logistics'" 
        @click="searchLogistics" 
        class="search-btn"
      >
        🔍 查询物流
      </button>
    </header>

    <main>
      <div v-if="loading" class="loading">加载数据中...</div>
      <div v-else-if="error" class="error">{{ error }}</div>
      
      <!-- Logistics Mode -->
      <div v-else-if="searchMode === 'logistics'">
        <LogisticsCard v-if="logisticsRecord" :record="logisticsRecord" />
        <div v-else class="empty">
          请输入追溯码并点击查询按钮
        </div>
      </div>
      
      <!-- Product Mode -->
      <div v-else class="product-grid">
        <ProductCard 
          v-for="product in filteredProducts" 
          :key="product.ProductId" 
          :product="product" 
        />
      </div>
      
      <div v-if="searchMode === 'product' && !loading && filteredProducts.length === 0" class="empty">
        未找到相关产品
      </div>
    </main>
  </div>
</template>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  gap: 30px;
}

.header {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 40px;
}

.subtitle {
  margin-top: -10px;
  margin-bottom: 20px;
  color: var(--text-secondary);
}

.loading, .error, .empty {
  padding: 40px;
  font-size: 1.2em;
  color: var(--text-secondary);
}

.error {
  color: #e74c3c;
}

.mode-toggle {
  display: flex;
  gap: 10px;
  margin-bottom: 20px;
}

.mode-toggle button {
  flex: 1;
  background: rgba(255, 255, 255, 0.3);
  color: var(--text-main);
  border: 2px solid transparent;
}

.mode-toggle button.active {
  background: var(--primary-color);
  color: white;
  border-color: var(--primary-color);
}

.search-btn {
  width: 100%;
  margin-top: 15px;
  font-size: 1.1em;
  padding: 12px;
}
</style>
