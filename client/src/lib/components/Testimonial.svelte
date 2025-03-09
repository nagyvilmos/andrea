<script>
    import { getTestimonial } from "../api/testimonial";
    import Bubble from "./Bubble.svelte";
    let id = $props()
</script>

{#await getTestimonial(id)}
    <br />
{:then testimonial}
    <div>
        <Bubble>
            <h2>{testimonial.statement}</h2>
        </Bubble>
        <p class="from">{testimonial.name} on {testimonial.date}</p>
    </div>
{:catch error}
    <br />
{/await}
<style>
    .from{
        text-align: right;
    }
</style>
