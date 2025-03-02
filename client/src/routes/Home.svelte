<script>
    import Carousel from "../lib/components/Carousel.svelte";

    const items = [
        "Feeling tired just as **you** get up?",
        "Searching for more energy constantly?",
        "Are **you** overwhelmed?",
        "Dreaming of having a good night's sleep?",
        "Not fealt well for some time?",
        "**You** want to change but cannot bring yourself to start it?"
    ];

</script>

<Carousel items={items} autoPlay={5000}/>
<p>
    As an experienced Health and Wellbeing coach, I would like to support <b
        >you</b
    >
    to develop a healthier lifestyle through improving its different aspects like
    eating habits, physical activity, stress management, sleep that hugely contribute
    to <b>you</b> feeling more energized, balanced, resilient, self-confident
    and generally being well. While <b>you</b> remain in the driving seat, I
    help to navigate to build up a positive mindset which ensures that
    <b>your</b> new healthy habits are enjoyable and sustainable.
</p>
<p>I offer:</p>
<ul>
    <li>Personalised wellbeing plans tailored to your goals.</li>
    <li>
        Guidance to help you eat more healthily; including nutrition plans based
        on balanced blood sugar
    </li>
    <li>One on one support</li>
    <li>Motivation and accountability to keep you on track.</li>
</ul>

<style>
    p,
    li {
        font-size: 1.2em;
        font-stretch: 1.2em;
    }
</style>
