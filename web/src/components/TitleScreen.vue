<script>
export default {
  props: ['wrong', 'correct'],
};
</script>
<template>
  <div class="text-black">
    <h1>Session over!</h1>
    <h3>{{ correct }} out of {{ wrong + correct }}</h3>
  </div>
</template>
