<script>
    const {main, sub, background} = $props();
</script>

<div class="button" style='--background:{background}'>
    <p class="button-main">{main}</p>
    <p class="button-sub">{sub}</p>
</div>        

<style>
.button {
  background:var(--background);
  padding:12px;
  border-radius:50%;
  width: 80px;
  height: 80px;
  text-align: center;
}
.button-main {
  font-size:48px;
  margin: 0;
  margin-top: -12px;
  top: 60px;
}
.button-sub {
  font-size:16px;
  margin: 0;
  top: 20px;
  margin-top: -12px;
}
</style>