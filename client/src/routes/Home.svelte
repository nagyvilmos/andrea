<script>
    import { marked } from "marked";

    const items = [
        "Feeling tired just as **you** get up?",
        "Searching for more energy constantly?",
        "Are **you** overwhelmed?",
        "Dreaming of having a good night's sleep?",
        "Not felt well for some time?",
        "**You** want to change but cannot bring yourself to start it?"
    ];

</script>

<table>
    <tbody>
        <tr><td colspan="2">{@html marked.parse(items[0])}</td></tr>
        <tr><td style="padding:24px 12px 18px 12px">{@html marked.parse(items[1])}</td><td style="padding:12px 24px 12px 18px">{@html marked.parse(items[2])}</td></tr>
        <tr><td style="padding:18px 12px 24px 12px">{@html marked.parse(items[3])}</td><td style="padding:12px 18px 12px 24px">{@html marked.parse(items[4])}</td></tr>
        <tr><td colspan="2">{@html marked.parse(items[5])}</td></tr>
    </tbody>
</table>
<div class="container">
    <div class="main">
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
    </div>
    <div class="aside">
        <img src="/home.svg" style={"width: 100%;"} />
    </div>
</div>

<style>
    p,
    li {
        font-size: 1.2em;
        font-stretch: 1.2em;
    }

    table {
        margin: 24px;
        font-family: var(--font-script);
        gap: 12px;
    }
    
    td {
        font-size: larger;
        text-align: center;
        width:50%;
    }
</style>
