import { posts } from '$lib/data.js';

export function load () {
	return ({
	summaries: posts.map( p => ({post : p.post, title: p.title}))	
})
}