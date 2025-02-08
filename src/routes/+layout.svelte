<script>
	import { page } from '$app/stores';
	import Header from "$lib/component/layout/header.svelte";
	let { children } = $props()
</script>

<svelte:head>
	<title>Andrea's Help</title>
	<meta name="description" content="Holistic health help" />
</svelte:head>

<Header currentPath={$page.url.pathname} />
<div class="content">
	{@render children()}
</div>

<style>
	div.content {
		background-color: white;
		border-radius:var(--border-radius);
		border-bottom: 2px solid #abc;
		opacity: 60%;
	}
</style>