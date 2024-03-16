import puppeteer from "puppeteer";
import { TradeEntry } from "../models/TradeEntry";


/**
 * This get's the most updated trades
 */
async function getMostRecentTradeData() {
    const browser = await puppeteer.launch({
        headless: true,
    });

    console.log("Puppeteer launched successfully.");

    const page = await browser.newPage();

    // Navigate the page to a URL
    await page.goto(
        "https://www.capitoltrades.com/trades?txType=buy&sortBy=-txDate&per_page=24"
    );

    // Set screen size
    await page.setViewport({ width: 1080, height: 1024 });

    // Wait for the table to be fully loaded and updated
    await page.waitForSelector("table.q-table");
    // Adjust the selector as per your webpage's structure

    // Extract data from the table
    const tableData: string[][] = await page.evaluate(() => {
        const rows = Array.from(document.querySelectorAll("table.q-table tbody tr"));
        return rows.map((row) => {
            const cells = Array.from(row.querySelectorAll("td"));
            return cells.map((cell) => cell.innerText.trim());
        });
    });
    // logger.info("got Raw table data");

    const formattedData: TradeEntry[] = formatToGoogleSheets(tableData);
    // logger.info(("Formatted table data"));
    await browser.close();

    return JSON.stringify(formattedData);
}


/* eslint-disable valid-jsdoc */
/**
 * Formats the data into nice rows.
 * @param {string[][]} tableData - The data to format into rows.
 * @returns {TradeEntry[]} An array of TradeEntry objects representing the formatted rows.
 */
function formatToGoogleSheets(tableData: string[][]): TradeEntry[] {
    return tableData.map((trade) => {
        const [politicianParty, issuerTicker, published, traded, filedAfter, owner, type, size, price] = trade.map((item) => item.split("\n").join(" "));

        // Split Politician and Party
        // Find the index of the last space character
        const lastSpaceIndex = politicianParty.lastIndexOf(" ");

        // Extract the politician"s name and political position
        const politician = politicianParty.slice(0, lastSpaceIndex);
        const politicalPosition = politicianParty.slice(lastSpaceIndex + 1);

        // Split Issuer and Ticker
        // Find the index of the last space character
        const lastSpaceIndexTicker = issuerTicker.lastIndexOf(" ");

        // Extract the politician's name and political position
        const issuer = issuerTicker.slice(0, lastSpaceIndexTicker);
        const ticker = issuerTicker.slice(lastSpaceIndexTicker + 1);
        // const [issuer, ticker] = issuerTicker.split('\n');

        // Parse dates
        const publishedDate = parseAndReplaceTodayDate(published);
        const tradedDate = parseAndReplaceTodayDate(traded);

        return {
            Politician: politician,
            Party: politicalPosition,
            Issuer: issuer,
            Ticker: ticker,
            Published: publishedDate,
            Traded: tradedDate,
            FiledAfter: filedAfter,
            Owner: owner,
            Type: type,
            Size: size,
            Price: price,
        };
    });
}


/**
 * Parses the input date string and replaces any occurrence of "Today" with the current date.
 * @param {string} dateString - The input date string to parse.
 * @return {string} The parsed date string with "Today" replaced by the current date.
 */
function parseAndReplaceTodayDate(dateString: string) {
    const parts = dateString.split("\n");
    const [day, month, year] = parts[0].split(" ");

    // Check if the date string contains "Today"
    if (day.toLowerCase() === "today") {
        const today = new Date();
        return `${today.getFullYear()} ${today.toLocaleString("default", { month: "short" })} ${today.getDate()}`;
    }

    return `${year} ${month} ${day}`;
}

async function run() {
    console.log(await getMostRecentTradeData());
}

run().catch(error => console.error(error));