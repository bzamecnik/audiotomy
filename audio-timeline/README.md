# TODO

- put the files into Gists/JSFiddle/CodePen
  - [Audio player with chord timeline](http://codepen.io/bzamecnik/pen/JKXyPx)

- [x] basic <audio> element
- [x] basic audio playback via the WebAudio API
- [x] basic playback with buttons
- [x] audio with D3js progress bar
- [x] audio with keyboard controls
  - like http://kolber.github.io/audiojs/demos/test6.html
- [x] seek by clicking into the progress bar
- [x] audio with synchronously displayed single row from a TSV file
- [x] audio with synchronously highlighted rows from a TSV file
- [x] audio with synchronous visualization
- [x] use `requestAnimationFrame` instead of `setInterval` for animation
  - http://www.paulirish.com/2011/requestanimationframe-for-smart-animating/
- [x] refactor the code and make it more modular
- [x] add titles to the chord columns in the timeline chart
  ```
  .append("svg:title")
    .text(function(d, i) { return d; });
  ```
- [x] add a cursor (just a vertical line)
- [x] use d3.dispatch to load data
  - https://bl.ocks.org/mbostock/5872848
- [x] solve a problem with different lengths of the audio and labels
- [x] make cursor draggable
  - http://bl.ocks.org/enjalot/1378144
- [x] get rid of the progress bar (when we have the cursor)
- chord time line with X zoom
- focus + context
  - http://bl.ocks.org/mbostock/1667367
  - [x] basic brushing - pan & zoom
  - [x] clipping
  - show the needle in the focus pane after brushing
  - automatic paging or scrolling
  - clean up the dirtied code
  - optimize the code - it seem to take a lot of CPU power
- reload with new data
- allow reordering by fifths
- allow specifying the key
- make the pitch classes relative to the key
- colorize the pitch classes
- audio with drag&drop file
- create a chart of the tone circle
- make panning bounded
  - http://computationallyendowed.com/blog/2013/01/21/bounded-panning-in-d3.html
- unique chords as nodes in graph, transitions as edges, force-directed layout

# segment viewer
- just view TSV with start,end,label + play audio

# segment editor
- allow creating & editing segments, save to TSV
