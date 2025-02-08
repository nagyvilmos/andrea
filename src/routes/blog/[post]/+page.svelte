<script>
	import { marked } from 'marked';
	let { data } = $props();
</script>

<h1>{data.post.title}</h1>
<div>{@html marked.parse(data.post.content)}</div>
