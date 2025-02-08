<script>
	let {data} = $props();
</script>

<h1>Blog</h1>

<ul>
	{#each data.summaries as {post, title}}
		<li><a href='/blog/{post}'>{title}</a></li>
	{/each}
</ul>