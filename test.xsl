<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:output method="xml" encoding="UTF-8"/>
<xsl:strip-space elements="*"/>
<xsl:template match="/">
  <table>
    <xsl:apply-templates select="*"/>
  </table>
</xsl:template>

<xsl:template match="*[text()]">
  <tr>
    <td>
    <xsl:for-each select="ancestor-or-self::*">
        <xsl:value-of select="name()" />
        <xsl:if test="position()!=last()">
            <xsl:text>_</xsl:text>
        </xsl:if>
    </xsl:for-each>
    </td>
    <td>
    <xsl:value-of select="." />
    </td>
  </tr>
    <xsl:text>&#10;</xsl:text>
    <xsl:apply-templates select="*"/>
</xsl:template>
</xsl:stylesheet>