import { error } from '@sveltejs/kit';
import { posts } from '$lib/data.js';

export function load ({params}) {
	let post = posts.find( p => p.post === params.post);
	if (!post)
	{
		error(404)
	}
	if (Array.isArray(post.content))
	{
		post= {...post};
		post.content = post.content.join('\n');
   }
   console.log('HERE BE DRAGONS')
   console.log({post})
   return {post}
}