export function load({ cookies }) {
	//import { setContext } from 'svelte';
	const visited = cookies.get('visited');
	//const homeShown = undefined;
	cookies.set('visited', 'true', { path: '/' });
	//setContext ('visited':false)
	return {
		visited
	};
}