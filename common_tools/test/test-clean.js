const assert = require('assert');
const { clean } = require('../converter.js');

describe('Convert from PO to JSON', () => {
    it('Replace double-escaped carriage return with line feed', () => {
        assert.equal(clean('First\\rSecond'), 'First\rSecond');
    });
});
