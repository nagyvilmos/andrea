<script>
	import Dialog from "$lib/component/dialog/dialog.svelte";
	import { text } from "$lib/component/dialog/config.js";
</script>

<Dialog title="Contact Us"
	config={{
		layout: [
			text("test", "Test Field")
		]
		
	}}

/>
