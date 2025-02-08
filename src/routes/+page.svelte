<script>
    let { data } = $props();

    const hello = `Hello ${data.visited ? 'friend' : 'stranger'}`
</script>


<h1>home</h1>
<p>{hello}.</p>