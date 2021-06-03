#!/usr/bin/node
// define a rectangle with valid attribute values

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || !w || !h) {
      const rect = {};
      return rect;
    } else {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
